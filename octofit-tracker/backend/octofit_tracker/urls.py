"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
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
from rest_framework.routers import DefaultRouter
from django.http import JsonResponse
import os
from . import views

# Register all viewsets with the router
router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'teams', views.TeamViewSet, basename='team')
router.register(r'activities', views.ActivityViewSet, basename='activity')
router.register(r'leaderboard', views.LeaderboardViewSet, basename='leaderboard')
router.register(r'workouts', views.WorkoutViewSet, basename='workout')

def api_root(request):
    # Use $CODESPACE_NAME for Codespaces, fallback to localhost for local dev
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        # Codespaces: use HTTPS, substitute the actual $CODESPACE_NAME value
        base_url = f"https://{codespace_name}-8000.app.github.dev"
    else:
        # Localhost: use HTTP
        base_url = "http://localhost:8000"
    return JsonResponse({
        "activities": f"{base_url}/api/activities/",
        "users": f"{base_url}/api/users/",
        "teams": f"{base_url}/api/teams/",
        "leaderboard": f"{base_url}/api/leaderboard/",
        "workouts": f"{base_url}/api/workouts/"
    })

from django.shortcuts import redirect

def root_redirect(request):
    return redirect('/api/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root_redirect),
    path('api/', api_root, name='api-root'),
    path('api/', include(router.urls)),
]
