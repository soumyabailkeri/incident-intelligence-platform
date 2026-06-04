from django.urls import path
from .views import IncidentListCreateAPIView

urlpatterns = [
    path(
        "incidents/",
        IncidentListCreateAPIView.as_view(),
        name="incident-list"
    ),
]