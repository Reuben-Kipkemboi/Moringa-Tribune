"""tribune URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import re_path as url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
#for tokens
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('news.urls')),
    
    #register
    url(r'^accounts/', include('django_registration.backends.one_step.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')), 
    url('logout/', auth_views.logout_then_login),

    #URLconf for the tinymce package.
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^api-token-auth/', obtain_auth_token)
]



if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

