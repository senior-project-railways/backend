"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include, re_path
# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from django.views import generic
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/users/', include('users.urls')),
    path('admin/', admin.site.urls),
    
    path('api/repairworks/', include(('repairworks.urls', 'repairworks'), namespace='repairworks-api')),
    path('api/trains/', include(('trains.urls', 'trains'), namespace='trains-api')),
    path('api/trainstations/', include(('trainstations.urls', 'trainstations'), namespace='trainstations-api')),
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api-token-auth/', obtain_jwt_token),
#     path('api-token-refresh/', refresh_jwt_token),
#     path('api/', include(('users.routers', 'users'), namespace='users-api')),
#     path('api/repairworks/', include(('repairworks.urls', 'repairworks'), namespace='repairworks-api')),
# ]
