"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from user_management.views import CustomConfirmEmailView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    # Schema generation and documentation views
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('api/auth/', include('dj_rest_auth.urls')), # login, logout, password reset
    path(
        'api/auth/registration/account-confirm-email/<str:key>/',
        CustomConfirmEmailView.as_view(),
        name='account_confirm_email',
    ),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')), # signup
    path('api/dj-rest-auth/', include('django.contrib.auth.urls')),
    # path('accounts/', include('user_management.urls'))
]
