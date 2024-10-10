from django.urls import path
from .views import CampaignCreateView

urlpatterns = [
    path('create-campaign/', CampaignCreateView.as_view(), name='create-campaign'),
]
