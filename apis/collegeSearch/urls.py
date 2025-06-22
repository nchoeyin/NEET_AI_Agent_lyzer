from django.urls import path
from .views import LyzrAgentApiAsyncView

urlpatterns = [
    path('lyzr-agent/', LyzrAgentApiAsyncView.as_view(), name='lyzr-agent')
] 