from approvedApplications import serialize
from approvedApplications.models import ApprovedApplications
from approvedApplications.serialize import ApprovedApplicationSerializer
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


class ApprovedApplicationsTable(APIView):
    def get(self, request):
        ApprovedApplicationObj = ApprovedApplications.objects.all()
        dlSerializeObj = ApprovedApplicationSerializer(
            ApprovedApplicationObj, many=True)
        return Response(dlSerializeObj.data)

    def post(self, request):
        serializeobj = ApprovedApplicationSerializer(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            subject = 'Congratulations, your scholarship has been approved'
            html_message = render_to_string(
                'status.html', {'status': request.data})
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


class SpecificApprovedApplications(APIView):
    def get(self, request, application_status):
        ApprovedApplicationObj = ApprovedApplications.objects.filter(
            application_status=application_status)

        dlSerializeObj = ApprovedApplicationSerializer(
            ApprovedApplicationObj, many=True)
        return Response(dlSerializeObj.data)

class SpecificApprovedApplicationsById(APIView):
    def get(self, request, pk):
        ApprovedApplicationObj = ApprovedApplications.objects.get(pk=pk)

        dlSerializeObj = ApprovedApplicationSerializer(
            ApprovedApplicationObj)
        return Response(dlSerializeObj.data)

class ApprovedApplicationUpdate(APIView):
    def post(self, request, pk):

        try:
            ApprovedApplicationObj = ApprovedApplications.objects.get(pk=pk)
        except:
            return Response("Not Found in Database")

        serializeobj = ApprovedApplicationSerializer(
            ApprovedApplicationObj, data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        return Response(serializeobj.errors)


class ApprovedApplicationDelete(APIView):
    def post(self, request, pk):
        try:
            ApprovedApplicationObj = ApprovedApplications.objects.get(pk=pk)
        except:
            return Response("Not Found in Database")
        ApprovedApplicationObj.delete()
        return Response(200)
