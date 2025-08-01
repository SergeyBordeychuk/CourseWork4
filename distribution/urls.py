from django.urls import path

from distribution.views import DistributionListView, RecipientListView, MessageListView, ContactTemplateView, \
    MessageCreateView, RecipientCreateView, DistributionCreateView, DistributionUpdateView, MessageUpdateView, \
    RecipientUpdateView, DistributionDeleteView, MessageDeleteView, RecipientDeleteView, send_mailing, count_main

app_name = 'distribution'

urlpatterns = [
    path('', DistributionListView.as_view(), name='distributions'),
    path('messages/', MessageListView.as_view(), name='messages'),
    path('recipients/', RecipientListView.as_view(), name='recipients'),
    path('contacts/', ContactTemplateView.as_view(), name='contacts'),
    path('message/create', MessageCreateView.as_view(), name='mes_create'),
    path('recipient/create', RecipientCreateView.as_view(), name='rec_create'),
    path('distribution/create', DistributionCreateView.as_view(), name='dis_create'),
    path('distribution/update/<int:pk>', DistributionUpdateView.as_view(), name='dis_update'),
    path('recipient/update/<int:pk>', RecipientUpdateView.as_view(), name='rec_update'),
    path('message/update/<int:pk>', MessageUpdateView.as_view(), name='mes_update'),
    path('distribution/delete/<int:pk>', DistributionDeleteView.as_view(), name='dis_delete'),
    path('recipient/delete/<int:pk>', RecipientDeleteView.as_view(), name='rec_delete'),
    path('message/delete/<int:pk>', MessageDeleteView.as_view(), name='mes_delete'),
    path('distribution/send_distribution/<int:pk>', send_mailing, name='send_dis'),
    path('distribution/send_data/', count_main, name='count'),
]