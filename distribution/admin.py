from django.contrib import admin
from distribution.models import Message, MailingRecipient, AttemptToSend, Distribution

# Register your models here.
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'theme',)

@admin.register(MailingRecipient)
class MailingRecipientAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'full_name',)

@admin.register(Distribution)
class DistributionAdmin(admin.ModelAdmin):
    list_display = ('id', 'status',)
    list_filter = ('id',)
    search_fields = ('status',)

@admin.register(AttemptToSend)
class AttemptToSendAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'response', 'distribution',)
    list_filter = ('id',)
    search_fields = ('status', 'response', 'distribution')