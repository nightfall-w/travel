from django.conf.urls import url
from .views import ResultList, ResultGrid, Detail, Schemes, ScenicSpot

urlpatterns = [
    url('^result-list/$', ResultList.as_view(), name='result-list'),
    url('^result-grid/$', ResultGrid.as_view(), name='result-grid'),
    url('^detail/(?P<id>[a-zA-Z0-9]{24})$', Detail.as_view(), name='detail'),
    url('^schemes/$', Schemes.as_view(), name='schemes'),
    url('^ScenicSpot/$', ScenicSpot.as_view(), name='Scenic_spot'),

]
