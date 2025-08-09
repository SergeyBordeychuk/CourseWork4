from msilib.schema import ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView
from django.core.mail import send_mail

from users.forms import CustomUserCreationForm, CustomUserUpdatePasswordForm
from users.models import CustomUser


# Create your views here.
class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('distribution:distribution')


    def form_valid(self, form):
        user = form.save()
        self.send_welcome_massage(user.email)
        return super().form_valid(form)


    def send_welcome_massage(self, user_email):
        subject = 'Добро пожаловать на наш сайт!'
        message = 'Регистрация прошла успешно!'
        from_email = 'sergeibordeichuk@yandex.ru'
        recipient_list = [user_email,]
        send_mail(subject, message, from_email, recipient_list)


def profile_info(request, pk):
    user = CustomUser.objects.get(pk=pk)
    context = {'username': user.username,
               'email': user.email,
               'phone': user.phone_number,
               'fullname': f'{user.first_name} {user.last_name}',
               'country': user.country,
               'pk': user.pk,
               }
    template_name = 'profile.html'
    return render(request, template_name, context)


class UserUpdatePasswordView(UpdateView, LoginRequiredMixin):
    model = CustomUser
    form_class = CustomUserUpdatePasswordForm
    template_name = 'change_password.html'
    success_url = reverse_lazy('distribution:distributions')
