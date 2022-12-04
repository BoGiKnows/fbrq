from rest_framework import generics
from rest_framework.response import Response

from .models import *
from .serializers import *
# Create your views here.


class MailDisListView(generics.ListAPIView):
    queryset = MailDis.objects.all()
    serializer_class = MailDisSerializer


class MailDisCreateView(generics.CreateAPIView):
    # queryset = MailDis.objects.all()
    serializer_class = MailDiscCreateSerializer

    def post(self, request, *args, **kwargs):
        # print(request.data)
        # tags = Tags.objects.filter(name__in=request.data.get('tags', ''))
        # print(list(tags.values()))
        # request.data['tags'] = list(tags.values())

        serializer = MailDiscCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        dis = serializer.save()
        return Response({'Ok. Номер рассылки': dis.id})
