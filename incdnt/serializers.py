from rest_framework import serializers
from .models import Incident

class IncidentSerializer(serializers.ModelSerializer):

    category_name = serializers.CharField(
        source="category.name",
        read_only=True
    )

    reported_by_username = serializers.CharField(
        source="reported_by.username",
        read_only=True
    )

    class Meta:
        model = Incident
        fields = "__all__"