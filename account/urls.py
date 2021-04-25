from django.urls import path

from .views import (
    AccountProfileView,
    CreateAccountView,
    LoginView,
    LogoutView,
)

app_name = 'account'
urlpatterns = [
    path('profile/', AccountProfileView.as_view(), name='profile'),
    path('create/', CreateAccountView, name='create'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
