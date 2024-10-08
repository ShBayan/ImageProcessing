"""DataScience URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

# from django.urls import path,include
from django.conf.urls import url, include
from rest_framework import routers
from django.contrib import admin

# from quickstart import views
# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

urlpatterns=[
    # url(r'^', include('snippets.urls')),
    url(r'^', include('images.urls')),
    # url(r'^', include('django_socketio.urls')),
    # url("", include('django_socketio.urls')),
]


# urlpatterns = [
#     path('polls/',include('polls.urls')),
#     path('admin/', admin.site.urls),
#
# ]

# url(r'^', include(router.urls)),
# url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
# url(r'^', include('snippets.urls')),