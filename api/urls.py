from django.conf.urls import url
from .views import Ticket

urlpatterns = [
    url('^getTicket/$', Ticket.as_view(), name='Ticket'),
]
