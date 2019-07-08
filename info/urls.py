from django.conf.urls import url
from .views import Result_list, Result_grid, Detail, Schemes, Scenic_spot

urlpatterns = [
    url('^result-list/$', Result_list.as_view(), name='result-list'),
    url('^result-grid/$', Result_grid.as_view(), name='result-grid'),
    url('^detail/$', Detail.as_view(), name='detail'),
    url('^schemes/$', Schemes.as_view(), name='schemes'),
    url('^ScenicSpot/$', Scenic_spot.as_view(), name='Scenic_spot'),

]
