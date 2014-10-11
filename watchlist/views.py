from rest_framework import viewsets
from watchlist.models import Show
from watchlist.serializers import ShowSerializer


class ShowViewSet(viewsets.ModelViewSet):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer
