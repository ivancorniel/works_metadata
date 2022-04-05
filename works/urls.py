from django.urls import path
from .views import ContributorsView

urlpatterns = [
    path('<str:iswc>', ContributorsView.as_view())
]