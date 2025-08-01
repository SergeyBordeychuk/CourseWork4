from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy

from distribution.models import Distribution, Message, MailingRecipient, AttemptToSend
from distribution.forms import DistributionForm, MessageForm, RecipientForm

from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.core.cache import cache
from django.views.decorators.cache import cache_page

from django.core.mail import send_mail
from django.conf import settings


class ContactTemplateView(TemplateView):
    template_name = 'contacts.html'


class MessageListView(ListView):
    model = Message
    template_name = 'message_list.html'
    context_object_name = 'messages'


class RecipientListView(ListView):
    model = MailingRecipient
    template_name = 'recipient_list.html'
    context_object_name = 'recipients'


class DistributionListView(ListView):
    model = Distribution
    template_name = 'distribution_list.html'
    context_object_name = 'distributions'


class DistributionCreateView(CreateView, LoginRequiredMixin):
    model = Distribution
    form_class = DistributionForm
    template_name = 'distribution_form.html'
    success_url = reverse_lazy('distribution:distributions')

    def form_valid(self, form):
        distribution = form.save()
        user = self.request.user
        distribution.owner = user
        distribution.save()
        return super().form_valid(form)


class MessageCreateView(CreateView, LoginRequiredMixin):
    model = Message
    form_class = MessageForm
    template_name = 'message_form.html'
    success_url = reverse_lazy('distribution:messages')

    def form_valid(self, form):
        distribution = form.save()
        user = self.request.user
        distribution.owner = user
        distribution.save()
        return super().form_valid(form)


class RecipientCreateView(CreateView, LoginRequiredMixin):
    model = MailingRecipient
    form_class = RecipientForm
    template_name = 'recipient_form.html'
    success_url = reverse_lazy('distribution:recipients')

    def form_valid(self, form):
        recipient = form.save()
        user = self.request.user
        recipient.owner = user
        recipient.save()
        return super().form_valid(form)


class DistributionUpdateView(UpdateView, LoginRequiredMixin):
    model = Distribution
    form_class = DistributionForm
    template_name = 'distribution_form.html'
    success_url = reverse_lazy('distribution:distributions')


class MessageUpdateView(UpdateView, LoginRequiredMixin):
    model = Message
    form_class = MessageForm
    template_name = 'message_form.html'
    success_url = reverse_lazy('distribution:messages')


class RecipientUpdateView(UpdateView, LoginRequiredMixin):
    model = MailingRecipient
    form_class = RecipientForm
    template_name = 'recipient_form.html'
    success_url = reverse_lazy('distribution:recipients')


class DistributionDeleteView(DeleteView, LoginRequiredMixin):
    model = Distribution
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('distribution:distribution')


class MessageDeleteView(DeleteView, LoginRequiredMixin):
    model = Message
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('distribution:messages')


class RecipientDeleteView(DeleteView, LoginRequiredMixin):
    model = MailingRecipient
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('distribution:recipients')

    
def send_mailing(request, pk):
    mailing = Distribution.objects.get(pk=pk)
    recipients = mailing.recipients.all()

    for recipient in recipients:
        try:
            mailing.status = 'Launched'
            mailing.save()
            send_mail(
                subject=mailing.message.theme,
                message=mailing.message.message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[recipient.email],
                fail_silently=False,
            )
            AttemptToSend.objects.create(status='Successfully', response='', distribution=mailing)
        except Exception as e:
            AttemptToSend.objects.create(status='Not successful', response=str(e), distribution=mailing)
    mailing.status = 'Completed'
    mailing.save()
    return redirect('distribution:distributions')


def count_main(request):
    recipients = []
    count_active_dis = 0
    for dist in Distribution.objects.get():
        if dist.status == 'Launched':
            count_active_dis += 1
        for recipient in dist.recipients:
            recipients.append(recipient)
    count_recipients = len(set(recipients))
    context= {'count_recipients': count_recipients, 'count_active_dist':count_active_dis}
    return render(request, 'distribution_list.html', context=context)
