from django.urls import path, re_path
from catalog.views import (index, ActorsListView, ActorDetailView, ProducerListView, ProducerDetailView,
                           FilmListView, FilmDetailView, SessionDetailView, reserve_ticket)

urlpatterns = [
    path('', index, name='index'),
    path('actors/', ActorsListView.as_view(), name='actors'),
    path('films/', FilmListView.as_view(), name='films'),
    path('producers/', ProducerListView.as_view(), name='producers'),
    path('tickets/reserve/<int:ticket_id>/', reserve_ticket, name='reserve_ticket'),

    re_path(r'^actors/(?P<pk>\d+)/$', ActorDetailView.as_view(), name='actor-detail'),
    re_path(r'^films/(?P<pk>\d+)/$', FilmDetailView.as_view(), name='film-detail'),
    re_path(r'^producers/(?P<pk>\d+)/$', ProducerDetailView.as_view(), name='producer-detail'),
    re_path(r'^sessions/(?P<pk>\d+)/$', SessionDetailView.as_view(), name='session-detail'),
    re_path(r'^ticket/(?P<pk>\d+)/$', SessionDetailView.as_view(), name='ticket-detail')
]