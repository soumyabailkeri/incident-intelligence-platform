from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    department = models.CharField(max_length=20)
    role = models.CharField(max_length=10, choices=[
        ('developer', 'Developer'),
        ('admin', 'Admin'),
        ('manager', 'Manager'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Priority(models.TextChoices):
    LOW = "LOW", "Low"
    MEDIUM = "MEDIUM", "Medium"
    HIGH = "HIGH", "High"
    CRITICAL = "CRITICAL", "Critical"

class Status(models.TextChoices):
    INITIATED = "INITIATED", "Initiated"
    IN_POOL_QUEUE = "IN_POOL_QUEUE", "In Pool Queue"
    ASSIGNED = "ASSIGNED", "Assigned"
    RESOLVED = "RESOLVED", "Resolved"
    CLOSED = "CLOSED", "Closed"
    REOPENED = "REOPENED", "Reopened"

class Incident(models.Model):
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    priority = models.CharField(
        max_length=20,
        choices=Priority.choices
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.INITIATED
    )
    reported_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="reported_incidents"
    )
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="assigned_incidents",
        null=True,
        blank=True
    )
    closed_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="closed_incidents",
        null=True,
        blank=True
    )
    resolution_summary = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    closed_at = models.DateTimeField(null=True, blank=True)
 
    def __str__(self):
        return self.title