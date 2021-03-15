from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import WordCountViewSet


router = DefaultRouter()
router.register('wordcount', WordCountViewSet)

app_name = 'app'

urlpatterns = [
    path('', include(router.urls))
]
