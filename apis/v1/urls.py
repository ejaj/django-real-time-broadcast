from django.urls import path

from apis.v1.views import MailchimpWebhookApiView

urlpatterns = [
    path('mailchimp-webhook/', MailchimpWebhookApiView.as_view()),
]
