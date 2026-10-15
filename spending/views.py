from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Sum

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions


from spending.serializers import UserSerializer,ExpenseSerializer
from spending.models import Expense
from spending.permissions import IsOwner
from spending.ai_service import get_budget_plan

from datetime import datetime

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

    # authentication_classes = [authentication.BasicAuthentication]

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):

        auth_user = request.user

        instance = User.objects.get(username=auth_user)

        serializer_instance = UserSerializer(instance)

        return Response(data=serializer_instance.data)

class ExpenseListCreateView(APIView):

    # authentication_classes = [authentication.BasicAuthentication]

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):

        instance  = Expense.objects.filter(owner=request.user)

        serializer = ExpenseSerializer(instance,many=True)

        return Response(data=serializer.data)

    def post(self,request):

        form_data = request.data

        serializer = ExpenseSerializer(data=form_data)

        if serializer.is_valid():

            serializer.save(owner=request.user)

            return Response(data=serializer.data)

        else: return Response(serializer.errors)


class ExpenseRetrieveUpdateDeleteView(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [IsOwner]

    def get(self,request,pk=None):

        instance = get_object_or_404(Expense,id=pk)

        self.check_object_permissions(request,instance)

        serializer = ExpenseSerializer(instance)

        return Response(data=serializer.data)

    def put(self,request,pk=None):

        instance = get_object_or_404(Expense,id=pk)

        self.check_object_permissions(request,instance)

        form_data = request.data

        serializer = ExpenseSerializer(data=form_data,instance=instance)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        else: return Response(serializer.errors)

    def delete(self,request,pk=None):

        instance = get_object_or_404(Expense,id=pk)

        self.check_object_permissions(request,instance)

        instance.delete()

        return Response({"message":"deleted.."})


class ExpenseSummary(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):

        response_data = {
            "todays_total":0,
            "monthly_total":0
        }

        current_date = datetime.now().date()

        # date() is an method while month,year is attribute

        current_month = datetime.now().month

        current_year = datetime.now().year

        monthly_transaction = Expense.objects.filter(owner=request.user,created_at__month=current_month,created_at__year=current_year)

        if monthly_transaction:

            monthly_total = monthly_transaction.values("amount").aggregate(total=Sum("amount")).get("total")


            monthly_category_summary = monthly_transaction.values("category").annotate(total=Sum("amount"))

            response_data["monthly_total"]=monthly_total

            response_data["monthly_category_summary"]= monthly_category_summary

        todays_transaction = Expense.objects.filter(owner=request.user,created_at__date=current_date)

        if todays_transaction:

            todays_total = todays_transaction.values("amount").aggregate(total=Sum("amount")).get("total")
            # no need of serializer since above query returns dict

            todays_category_summary = todays_transaction.values("category").annotate(total=Sum("amount"))



            response_data['todays_total'] = todays_total

            response_data["todays_category_summary"] = todays_category_summary

        
        return Response(data=response_data)


class BudgetPlanView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):

        response_data = {
            "monthly_total":0
        }

        current_month = datetime.now().month
        current_year = datetime.now().year

        monthly_transactions= Expense.objects.filter(owner=request.user,created_at__month=current_month,created_at__year=current_year)

        if monthly_transactions :

            monthly_total = monthly_transactions.values("amount").aggregate(total=Sum("amount")).get("total")

            category_summary = monthly_transactions.values("category").annotate(total=Sum("amount"))

            response_data["monthly_total"] = monthly_total

            response_data["category_summary"] = category_summary

            budgetplan = get_budget_plan(response_data)

            response_data["Plan"] = budgetplan
            
        return Response(data=response_data)
