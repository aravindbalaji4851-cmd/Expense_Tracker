from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from spending.serializers import UserSerializer


class SignUpView(APIView):

    def post(self,request):

        form_data = request.data

        serializer_inst = UserSerializer(data=form_data)

        if serializer_inst.is_valid():

            cleaned_data = serializer_inst.validated_data

            qs = User.objects.create_user(**cleaned_data)

            instance = UserSerializer(qs)

            return Response(data=instance.data)

        else: return Response(data=serializer_inst.errors)

        
class GetMeView(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):

        auth_user = request.user

        instance = User.objects.get(username=auth_user)

        serializer_instance = UserSerializer(instance)

        return Response(data=serializer_instance.data)
