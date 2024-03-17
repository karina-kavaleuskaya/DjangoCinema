from django.shortcuts import render, redirect, get_object_or_404
from catalog.models import Film, Actors, Producer, Genre, Session, Ticket
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required


def index(request):
    num_films = Film.objects.all().count()
    num_actors = Actors.objects.all().count()
    num_producer = Producer.objects.all().count()
    num_session = Session.objects.all().count()
    num_ticket = Ticket.objects.all().count()
    num_ticket_available = Ticket.objects.filter(status__exact='Available').count()

    return render(request, 'index.html', {
        "num_films": num_films,
        "num_actors": num_actors,
        "num_producer": num_producer,
        "num_session": num_session,
        "num_ticket": num_ticket,
        "num_num_ticket_available": num_ticket_available

    })


class ActorsListView(ListView):
    model = Actors
    template_name = 'actors_list.html'
    context_object_name = 'actors_list'


class ActorDetailView(DetailView):
    model = Actors
    template_name = "actor_detail.html"


class ProducerListView(ListView):
    model = Producer
    template_name = 'producer_list.html'
    context_object_name = 'producer_list'


class ProducerDetailView(DetailView):
    model = Producer
    template_name = "producer_detail.html"


class FilmListView(ListView):
    model = Film
    template_name = 'films_list.html'
    context_object_name = 'films_list'


class FilmDetailView(DetailView):
    model = Film
    template_name = "film_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sessions'] = Session.objects.filter(film=self.object)
        return context


class SessionDetailView(DetailView):
    model = Session
    template_name = 'session_detail.html'


@login_required
def reserve_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    film = ticket.film

    user_age = request.user.age
    if user_age >= film.age:
        try:
            if ticket.status == 'Available':
                ticket.status = 'On Loan'
                ticket.borrower = request.user
                ticket.save()

                user = request.user
                user.bookings.add(ticket)

                return redirect('reserve_ticket')
            else:
                return render(request, 'reserve_error.html', {'error': 'This ticket is already reserved.'})
        except Exception as e:
            return render(request, 'reserve_ticket.html', {'error': str(e)})
    else:
        return render(request, 'reserve_error.html', {'error': 'You are not old enough to reserve this film.'})
