from applicationDetails import serialize
from applicationDetails.models import Applications
from applicationDetails.serialize import ApplicationDetailSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class ApplicationDetailTable(APIView):
    def get(self, request):
        ApplicationDetailsObj = Applications.objects.all()
        dlSerializeObj = ApplicationDetailSerializer(ApplicationDetailsObj, many=True)
        return Response(dlSerializeObj.data)

    def post(self, request):
        serializeobj = ApplicationDetailSerializer(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        return Response(serializeobj.errors)

class SpecificApplicationDetailsTable(APIView):
    def get(self, request, pk):
        ApplicationDetailsObj = Applications.objects.get(pk=pk)

        dlSerializeObj = ApplicationDetailSerializer(ApplicationDetailsObj, many=False)
        return Response(dlSerializeObj.data)

class ApplicationDetailsUpdate(APIView):
    def post(self, request, pk):

        try:
            ApplicationDetailsObj = Applications.objects.get(pk=pk)
        except:
            return Response("Not Found in Database")

        serializeobj = ApplicationDetailSerializer(
            ApplicationDetailsObj, data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        return Response(serializeobj.errors)


class ApplicationDetailsDelete(APIView):
    def post(self, request, pk):
        try:
            ApplicationDetailsObj = Applications.objects.get(pk=pk)
        except:
            return Response("Not Found in Database")
        ApplicationDetailsObj.delete()
        return Response(200)
