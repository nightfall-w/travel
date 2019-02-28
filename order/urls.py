from django.conf.urls import url

from .views import Payment, Confirmation

urlpatterns = [
    url('^payment/$', view=Payment.as_view(), name='payment'),
    url('^confirmation/$', view=Confirmation.as_view(), name='confirmation'),
]
