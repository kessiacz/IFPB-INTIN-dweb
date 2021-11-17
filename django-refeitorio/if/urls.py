"""if URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from funcionario import views as viewsfunc
from django.contrib.auth import views as auth_views
from reifeicao import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.UserLoginView.as_view(template_name='login.html'), name='users-signin'),
    path('logout/', auth_views.LogoutView.as_view(), name='users-signout'),
    path('signup/', views.UserCreateView.as_view(), name='users-signup'),

    path('form/', views.FormListView.as_view(), name='requets-caest'),
    path('form/<int:pk>/', views.ReqDetailView.as_view(), name='process-detail'),
    path('professor/', views.FormProfDetailView.as_view(), name='request-teacher'),
    path('request/', views.ReIFCreateView.as_view(), name='request-form'),
    
    path('register/', views.UserCreateView.as_view(), name='users-signup'),

    
    #path('register/', views.register_page),
]
urlpatterns += staticfiles_urlpatterns()


