"""
URL configuration for mountain_passes project.

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
from passes.views import submit_data, get_pereval, edit_pereval, get_user_perevals
from passes import swagger

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include([
        path('submit_data/', submit_data, name='submit_data'),
        path('submitData/<int:id>/', get_pereval, name='get_pereval'),
        path('submitData/<int:id>/edit/', edit_pereval, name='edit_pereval'),
        path('submitData/', get_user_perevals, name='get_user_perevals'),
    ])),
    # Добавляем путь к Swagger API
    path('', include('passes.swagger')),
]
