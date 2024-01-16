"""
URL configuration for adBoard project.

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
from ads.views import *
from accounts.views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ads/', AdList.as_view(), name='ads'),
    path('ads/<int:pk>', AdDetails.as_view(), name='ad'),
    path('ads/new', AdNew.as_view(), name='ad_new'),
    path('ads/<int:ad_id>/new-response/', ResponseNew.as_view(), name='new-response'),
    path('my_responses/', Responses.as_view(), name='my_responses'),
    # path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),
    path('register/', register, name='register'),
    path('confirm_code/<str:email>/', confirm_code, name='confirm_code'),
    path('resend_code/<str:email>/', resend_code, name='resend_code'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('accept_response/<int:response_id>/', accept_response, name='accept_response'),
    path('ads/<int:pk>/update', AdUpdate.as_view(), name='ad_update'),
    path('ads/<int:pk>/delete', AdDelete.as_view(), name='ad_delete'),
    path('my_responses/<int:pk>/delete', ResponseDel.as_view(), name='delete_response'),
]
