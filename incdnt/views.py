from rest_framework import generics
from incdnt.models import Incident
from incdnt.serializers import IncidentSerializer

class IncidentListCreateAPIView(
    generics.ListCreateAPIView
):

    queryset = Incident.objects.all()

    serializer_class = IncidentSerializer