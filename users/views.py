from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.core.mail import send_mail

from users.forms import CustomUserCreationForm


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
