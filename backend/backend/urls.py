from django.http import JsonResponse
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register('tasks', views.TaskView, 'task')

urlpatterns = [
    path('', lambda request: JsonResponse({"status": "ok"})),
    path('admin/', admin.site.urls),

    # API
    path('api/', include(router.urls)),

    # USERS (ВАЖНО: именно users.urls)
    path('api/users/', include('djoser.urls')),

    # AUTH TOKEN
    path('api/auth/', include('djoser.urls.authtoken')),
]
