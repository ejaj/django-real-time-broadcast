from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class MandrillEvents(models.Model):
    message_id = models.CharField(_('Message ID'), null=True, blank=True, max_length=250)
    event_name = models.CharField(_('Event Name'), null=True, blank=True, max_length=250)
    subject = models.CharField(_('Subject'), null=True, blank=True, max_length=250)
    email = models.EmailField(_('Email'), null=True, blank=True)
    sender = models.EmailField(_('Sender'), null=True, blank=True)
    tags = models.JSONField(_('Tags'), null=True, blank=True)
    state = models.CharField(_('State'), null=True, blank=True, max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']
        db_table = 'mandrill_events'

    def __str__(self):
        return str(self.message_id) + str(self.event_name)
