from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q, Sum, Count
from . import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

class TestApi(APIView):
    def get(self, request):
        print("GET")
        obj = models.test.objects.filter(id=3).first()
        se = serializers.TestApi(obj, many=True)
        return Response(se.data, status.HTTP_200_OK)

    def post(self, request):
        print("POST")
        se = serializers.TestApi(data=request.data)
        if se.is_valid():
            se.save()
            return Response(se.data, status.HTTP_200_OK)
        return Response(se.errors, status.HTTP_400_BAD_REQUEST)

def test(request):
    obj = models.test(firstname= "Mohammad", lastname="Nazari")
    obj.save()
    return HttpResponse("Hello world!")

def get_test(request):
    objs = models.test.objects.all()
    print(objs)
    return HttpResponse("Hello world!")


def page1(request, num):
    temp = loader.get_template("test.html")
    # fname =request.GET["fname"]
    # lname =request.GET["lname"]
    # obj = models.test(firstname= fname, lastname=lname)
    # obj.save()
    obj = models.test.objects.all()[0]
    # obj = models.test.objects.get(id=num)
    # obj = models.test.objects.filter(id=num).first()
    # obj.lastname = request.GET["lname"]
    # obj.save()
    
    # obj = models.test.objects.filter(id=num).first()
    # obj.delete()

    # print(len(obj))


    objs = models.test.objects.all()

    return HttpResponse(temp.render({"objs": objs}))

def page2(request):

    obj = models.test.objects.filter(id__gte=1).order_by("-id").exclude(lastname="Mosavi").values()
    obj = models.test.objects.filter(Q(id__gte=1), Q(id=3)).values()
    obj = models.test.objects.values('firstname').annotate(count=Sum("id"))
    obj = models.test.objects.filter(address__st="Tehran").values()
    print(obj)


    tmp = loader.get_template('page2.html')
    return HttpResponse(tmp.render({"var2":2}))
