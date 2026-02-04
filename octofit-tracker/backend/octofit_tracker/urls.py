"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
import os
from rest_framework import routers
from .views import UserViewSet, TeamViewSet, ActivityViewSet, WorkoutViewSet, LeaderboardViewSet

def api_root(request):
    codespace_name = os.environ.get('CODESPACE_NAME', 'localhost')
    if codespace_name and codespace_name != 'localhost':
        api_url = f"https://{codespace_name}-8000.app.github.dev/api/"
    else:
        api_url = "http://localhost:8000/api/"
    return JsonResponse({
        "activities": f"{api_url}activities/",
        "teams": f"{api_url}teams/",
        "users": f"{api_url}users/",
        "leaderboard": f"{api_url}leaderboard/",
        "workouts": f"{api_url}workouts/"
    })

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'leaderboard', LeaderboardViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', api_root),
    path('', api_root),
]
