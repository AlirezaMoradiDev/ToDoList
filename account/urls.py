from django.urls import path
from . import views
from rest_framework.authtoken import views as authView


app_name = 'account'
urlpatterns = [
    path('logout', views.logout_user, name='logout'),
    path('edit', views.edit_user, name='edit'),
    path('reg', views.register_user, name='signup'),
    path('api', views.user_api, name='api'),
    path('token', authView.obtain_auth_token)

]
