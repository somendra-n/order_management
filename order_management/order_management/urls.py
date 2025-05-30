
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),

    # API routes for order management
    path('api/', include('orders.urls')),

    # Authentication routes (login, logout, password reset, etc.)
    path('auth/', include('dj_rest_auth.urls')),

    # User registration endpoint
    path('auth/registration/', include('dj_rest_auth.registration.urls')),

    # Allauth routes (handles Google social login, etc.)
    path('accounts/', include('allauth.urls')),

    # This handles the redirect URL after a successful login
    path('accounts/profile/', lambda request: HttpResponse("✅ Logged in successfully via Google or other provider")),

    # Root route (homepage or welcome page)
    path('', lambda request: HttpResponse("👋 Welcome to the Order Management System")),
]
