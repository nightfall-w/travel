from graphene_django.views import GraphQLView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin


class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class PublicGraphQLView(GraphQLView):
    pass
