from django.conf.urls import url
from .views import *

urlpatterns = [
    url('^about/$', view=Presentation.as_view(), name='about'),
    url('^FAQ/$', view=FAQ.as_view(), name='FAQ'),
    url('^contact/$', view=Contact.as_view(), name='contact'),
    url('^static/$', view=Static.as_view(), name='static'),
]
