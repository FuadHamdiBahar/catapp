from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView


# models
from django.contrib.auth.models import User

# Create your views here.


def CreateAccountView(request, *args, **kwargs):
    context = {}
    if request.method == 'GET':
        pass
        print(User.objects.all())
        # print('masuk pak eko')

    if request.method == 'POST':
        form = request.POST
        print(form['username'])
        new_user = User(
            first_name=form['fullname'],
            username=form['username'],
            password=make_password(form['password'])
        )
        new_user.save()
        success_url = reverse_lazy('account:login')
        return HttpResponseRedirect(success_url)

    return render(request, 'account/create.html', context)


class AccountProfileView(TemplateView):
    template_name = 'account/profile.html'


class LoginView(LoginView):
    template_name = 'account/login.html'


class LogoutView(LogoutView):
    template_name = 'account/logout.html'
