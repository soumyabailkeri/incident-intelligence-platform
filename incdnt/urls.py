from django.urls import path
from .views import (
    IncidentListCreateAPIView,
    IncidentDetailAPIView
)

urlpatterns = [
    path(
        "incidents/",
        IncidentListCreateAPIView.as_view(),
        name="incident-list"
    ),

    path(
        "incidents/<int:pk>/",
        IncidentDetailAPIView.as_view(),
        name="incident-detail"
    ),
]