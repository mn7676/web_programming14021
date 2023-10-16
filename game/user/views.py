from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import models

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

