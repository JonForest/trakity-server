"""trakity_main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.http import HttpResponse
from django.urls import path
from django.conf.urls import include
from trakity_main.views import TaskViewSet

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('status/ping', lambda _: HttpResponse('ping')),
    # See https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset for details
    path('tasks', TaskViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('tasks/<int:pk>', TaskViewSet.as_view({'get': 'retrieve', 'patch': 'update'})),
    path('auth/', include('usertokenauth.urls', namespace='usertokenauth')),
]

# https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/#adding-login-to-the-browsable-api
# todo: This allows the Rest Framework web interface to provide a login button. Should probably be removed at some point
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
