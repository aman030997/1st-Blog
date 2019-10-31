"""Aman URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https:/docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path,include,re_path
from django.conf.urls import include, url
from users import views as user_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',user_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('',include('mypoll.urls')),

    re_path(r'^password_reset/$', auth_views.PasswordResetView.as_view
        (template_name= "mypoll/password_reset_form.html"),
        name='password_reset'),

    re_path(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view
        (template_name= "mypoll/password_reset_done.html"),
        name='password_reset_done'),

    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view
        (template_name= "mypoll/password_reset_confirm.html"),
        name='password_reset_confirm'),
    
    re_path(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view
        (template_name= "mypoll/password_reset_complete.html"),
        name='password_reset_complete'),
    
    #re_path(r'^', include('django.contrib.auth.urls')), # for including all auths then we can ignore line 26-30
]
