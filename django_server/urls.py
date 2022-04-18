from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from joke.views import JokeViewSet

router = DefaultRouter()
router.register('joke', JokeViewSet, basename='joke')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
