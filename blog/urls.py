from django.conf.urls import url
from .views import blog, single

urlpatterns = [
    url('^list/$', view=blog.as_view(), name='list'),
    url('^single/$', view=single.as_view(), name='single'),
]
