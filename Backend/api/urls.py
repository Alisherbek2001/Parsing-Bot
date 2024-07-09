from django.urls import path
from .views import PostAPIView

urlpatterns = [
    path('', PostAPIView.as_view(), name='posts'),
    path('<int:pk>/', PostAPIView.as_view(), name='post-detail'),
]
