from . import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
import random

persian_alphabet = ['ا', 'ب', 'پ', 'ت', 'ث', 'ج', 'چ', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'ژ', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ک', 'گ', 'ل', 'م', 'ن', 'و', 'ه', 'ی']


class Participations(APIView):
    Serializer = serializers.Participation
    Model = models.Participation

    def post(self, request):

        print(request.user)
        objs = models.Competition.objects.filter(complete=False).exclude(user=request.user).order_by('create_date')

        if len(objs) > 0:
            comp = objs.first()
            comp.complete = True
            comp.save()
        else:
            comp = models.Competition(alphabet=random.choice(persian_alphabet))
            comp.save()

        data = {
            "player": request.user.id,
            "competition": comp.id
        }
        serializer = self.Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        # participation = models.Participation()
        # data = {
        #     ""
        # }
        # username = request.data["username"]
        # password = request.data["password"]
        # phone = request.data["phone"]
        #
        # user = models.User.objects.create_user(username=username, phone=phone, is_staff=True, password=password)
        # user.save()

        return Response({}, status.HTTP_204_NO_CONTENT)
        # print("POST")
        # se = serializers.TestApi(data=request.data)
        # if se.is_valid():
        #     se.save()
        #     return Response(se.data, status.HTTP_200_OK)
        # return Response(se.errors, status.HTTP_400_BAD_REQUEST)
