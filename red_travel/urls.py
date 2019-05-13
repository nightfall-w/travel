"""red_travel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from graphql_access.view import PublicGraphQLView, PrivateGraphQLView

from info.views import Index
from .schema import public_schema, private_schema

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^info/', include('info.urls', namespace='info')),
    url(r'^purview/', include('user.urls', namespace='purview')),
    url(r'^order/', include('order.urls', namespace='order')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^avow/', include('avow.urls', namespace='avow')),
    url(r'^social/', include('social_django.urls', namespace='social')),
    url(r'^graphql/', PublicGraphQLView.as_view(graphiql=True, schema=public_schema)),
    url(r'^private_graphql/', PrivateGraphQLView.as_view(graphiql=True, schema=private_schema)),
    # url(r'^graphql/', PrivateGraphQLView.as_view(graphiql=True, schema=schema)),
    url(r'^$', Index.as_view(), name='index'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
