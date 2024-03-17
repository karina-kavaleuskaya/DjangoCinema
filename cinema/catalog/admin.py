from django.contrib import admin
from catalog.models import Film, Genre, Actors, Producer, Session, Ticket


class FilmInLine(admin.TabularInline):
    model = Film


class FilmActorsInline(admin.TabularInline):
    model = Film.actors.through
    extra = 1


class SessionInLine(admin.StackedInline):
    model = Session


class TicketInLine(admin.StackedInline):
    model = Ticket


class ActorsAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']



class ProducerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']
    inlines = [FilmInLine]


class FilmAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'display_genre']
    inlines = [FilmActorsInline]


class SessionAdmin(admin.ModelAdmin):
    list_display = ['film', 'hall', 'timetable']
    inlines = [TicketInLine]


class TicketAdmin(admin.ModelAdmin):
    list_display = ['status', 'price', 'session_id', 'isbn']


admin.site.register(Genre)
admin.site.register(Actors, ActorsAdmin)
admin.site.register(Producer, ProducerAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Film, FilmAdmin)
