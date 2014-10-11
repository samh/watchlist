from watchlist.models import Show
from rest_framework import serializers


class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Show
