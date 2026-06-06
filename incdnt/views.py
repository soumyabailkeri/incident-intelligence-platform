from rest_framework import generics
from incdnt.models import Incident
from incdnt.serializers import IncidentSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsManagerOrAdmin

class IncidentListCreateAPIView(
    generics.ListCreateAPIView
):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    permission_classes = [IsAuthenticated]


class IncidentDetailAPIView(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    permission_classes = [IsAuthenticated]

class IncidentListCreateAPIView(
    generics.ListCreateAPIView
):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    permission_classes = [IsManagerOrAdmin]