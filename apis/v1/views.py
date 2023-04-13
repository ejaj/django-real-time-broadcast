import json
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt

from home.models import MandrillEvents


class MailchimpWebhookApiView(APIView):
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        data = request.data
        events = data.get('mandrill_events')
        for event in events:
            event_name = event.get('event')
            msg = event.get('msg')
            obj, created = MandrillEvents.objects.update_or_create(
                message_id=msg['_id'] if msg and msg['_id'] else None,
                defaults={
                    'event_name': event_name,
                    'subject': msg['subject'] if msg and msg['subject'] else None,
                    'email': msg['email'] if msg and msg['email'] else None,
                    'sender': msg['sender'] if msg and msg['sender'] else None,
                    'tags': json.dumps(msg['tags']) if msg and msg['tags'] else None,
                    'state': msg['state'] if msg and msg['state'] else None,
                },
            )
        return Response({'success': True})
