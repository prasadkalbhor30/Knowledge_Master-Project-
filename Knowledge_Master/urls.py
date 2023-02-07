"""Knowledge_Master URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from .views import *
from django.conf.urls import include
from Online_Test import urls as online_urls
from courses import urls as courses_urls
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',home),
    path('about/',about,name="about"),
    path('sign-up/',signUp,name="sign-up"),
    path('save-user/',save_User,name="save-user"),
    path('sign-in/',signIn,name="sign-in"),
    path('logout/',logOut,name="logout"),
    path('validate-user/',validateUser,name="validate-user"),
    path('contact/',contact,name="contact"),
    path('online-test/',include(online_urls),name="online-test"),
    path('courses/',include(courses_urls),name="courses"),
    path('admin/', admin.site.urls,name="admin"), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




