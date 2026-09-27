from django.urls import path
from .views import ResumeAnalysis

urlpatterns = [
    path('details/',ResumeAnalysis.as_view())
]
