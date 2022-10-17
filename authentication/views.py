from django.shortcuts import render
from authentication import serializers
from djoser import email
from authentication.models import UserAccount
from authentication.serializers import UserCreateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class AllUsersDetailsTable(APIView):
    def get(self, request):
        UsersInfoObj = UserAccount.objects.all()

        dlSerializeObj = UserCreateSerializer(UsersInfoObj, many=True)
        return Response(dlSerializeObj.data)


class UsersDetailsTables(APIView):
    def get(self, request, pk):
        UsersInfoObj = UserAccount.objects.get(pk=pk)

        dlSerializeObj = UserCreateSerializer(UsersInfoObj)
        return Response(dlSerializeObj.data)


class UsersEmailDetailsTables(APIView):
    def get(self, request, email):
        UsersInfoObj = UserAccount.objects.get(email=email)

        dlSerializeObj = UserCreateSerializer(UsersInfoObj)
        return Response(dlSerializeObj.data)


class UsersDetailsUpdate(APIView):
    def post(self, request, email):

        try:
            UsersInfoObj = UserAccount.objects.get(email=email)
        except:
            return Response("Not Found in Database")

        serializeobj = UserCreateSerializer(
            UsersInfoObj, data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        return Response(serializeobj.errors)


class UsersDetailsDelete(APIView):
    def post(self, request, pk):
        try:
            UsersInfoObj = UserAccount.objects.get(pk=pk)
        except:
            return Response("Not Found in Database")
        UsersInfoObj.delete()
        return Response(200)
