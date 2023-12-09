from . import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from datetime import timedelta
from . import serializers
from rest_framework.permissions import IsAuthenticated
from .permission import IsAdmin
import random

persian_alphabet = ['ا', 'ب', 'پ', 'ت', 'ث', 'ج', 'چ', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'ژ', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ',
                    'ع', 'غ', 'ف', 'ق', 'ک', 'گ', 'ل', 'م', 'ن', 'و', 'ه', 'ی']


class Participations(APIView):
    Serializer = serializers.Participation
    Model = models.Participation

    def post(self, request):

        print(request.user)
        print(models.Competition.objects.filter(complete=True).first().participation_set.all())
        objs = models.Competition.objects.filter(complete=False)\
            .exclude(id__in=models.Participation.objects.filter(player=request.user).values('competition'))\
            .order_by('create_date')

        print(objs)

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


class PaperCompetition(APIView):
    Serializer = serializers.Paper
    Model = models.Paper
    # permission_classes = (IsAuthenticated,)

    def post(self, request, cid):

        t = timezone.now() - timedelta(minutes=1)
        # participation = models.Participation.objects.filter(player=request.user, competition_id=cid, date__gte=t).first()
        participation = models.Participation.objects.filter(player=request.user, competition_id=cid).first()


        if participation is None:
            return Response({}, status.HTTP_404_NOT_FOUND)
        else:
            data = {
                "type": request.data["type"],
                "value": request.data["value"],
                "player": request.user.id,
                "competition": cid
            }
            serializer = self.Serializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status.HTTP_200_OK)
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class Score(APIView):
    Serializer = serializers.Paper
    Model = models.Paper
    permission_classes = (IsAdmin,)

    def post(self, request, pid):
        print("OK")
        return Response({}, status.HTTP_200_OK)
