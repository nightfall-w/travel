from django.conf.urls import url
from .views import UserLogin, UserRegister, UserLogout, Set_password, Update_photo
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    url(r'^login/$', UserLogin.as_view(), name='login'),
    url(r'^accounts/login/$', UserLogin.as_view(), name='accounts_login'),
    url(r'^logout/$', UserLogout.as_view(), name='logout'),
    url(r'^register/$', UserRegister.as_view(), name='register'),
    url(r'^update_photo/$', Update_photo.as_view(), name='update_photo'),
    url(r'^set_password/$', Set_password.as_view(), name='set_password'),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-auth_refresh/', refresh_jwt_token),
]
