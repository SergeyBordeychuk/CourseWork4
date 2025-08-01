from django.forms import ModelForm

from distribution.models import Message, MailingRecipient, Distribution


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['theme', 'message',]

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['theme'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Введите тему сообщения',
        })
        self.fields['message'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите сообщение',
        })


class RecipientForm(ModelForm):
    class Meta:
        model = MailingRecipient
        fields = ['email', 'full_name', 'comment',]

    def __init__(self, *args, **kwargs):
        super(RecipientForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Введите почту',
        })
        self.fields['full_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите полное имя',
        })
        self.fields['comment'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите комментарий',
        })


class DistributionForm(ModelForm):
    class Meta:
        model = Distribution
        fields = ['message', 'recipients',]

    def __init__(self, *args, **kwargs):
        super(DistributionForm, self).__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите сообщение',
        })
        self.fields['recipients'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите получателя',
        })