from sponsoredApplications import serialize
from sponsoredApplications.models import SponsoredApplications
from sponsoredApplications.serialize import SponsoredApplicationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# sending mails
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.dispatch import receiver
from django.template import Context
from django.template.loader import get_template
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class SponsoredApplicationsTable(APIView):
    def get(self, request):
        SponsoredApplicationsObj = SponsoredApplications.objects.all()
        dlSerializeObj = SponsoredApplicationSerializer(SponsoredApplicationsObj, many=True)
        return Response(dlSerializeObj.data)

    def post(self, request):
        serializeobj = SponsoredApplicationSerializer(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            subject = 'Congratulations, your have recieved scholarship award'
            html_message = render_to_string(
                'Congratulations.html', {'scholarship': request.data})
            plain_message = strip_tags(html_message)
            from_email = 'Scholarship Status <dontestsystem@gmail.com>'
            to = 'kibetdonald97@gmail.com'
            # to = tosend.clientEmail
            msg = EmailMultiAlternatives(subject, plain_message, from_email,
                                         [to])
            msg.attach_alternative(html_message, "text/html")
            msg.attach_file("Scholarship Attachment.pdf")
            msg.send()
            return Response(200)
        return Response(serializeobj.errors)

class SpecificSponsoredApplications(APIView):
    def get(self, request, pk):
        ApplicationDetailsObj = Applications.objects.get(pk=pk)

        dlSerializeObj = ApplicationDetailSerializer(ApplicationDetailsObj, many=False)

class SponsoredApplicationUpdate(APIView):
    def post(self, request, pk):

        try:
            SponsoredApplicationsObj = SponsoredApplications.objects.get(pk=pk)
        except:
            return Response("Not Found in Database")

        serializeobj = SponsoredApplicationSerializer(
            SponsoredApplicationsObj, data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        return Response(serializeobj.errors)


class SponsoredApplicationDelete(APIView):
    def post(self, request, pk):
        try:
            SponsoredApplicationsObj = SponsoredApplications.objects.get(pk=pk)
        except:
            return Response("Not Found in Database")
        SponsoredApplicationsObj.delete()
        return Response(200)
