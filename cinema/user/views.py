from django.contrib.auth import login
from django.shortcuts import render, redirect
from user.forms import RegistrationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from catalog.models import Ticket


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'registration/signup.html', {'form': form})


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = "user_profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user
        context['bookings'] = Ticket.objects.filter(borrower=user)
        return context
