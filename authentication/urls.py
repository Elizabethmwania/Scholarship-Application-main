"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views
from django.contrib.auth.models import Group  # new
from social_django.models import Association, Nonce, UserSocialAuth

urlpatterns = [
    path('', views.AllUsersDetailsTable.as_view()),
    path('<int:pk>', views.UsersDetailsTables.as_view()),
    path('<str:email>', views.UsersEmailDetailsTables.as_view()),
    path('update/<str:email>', views.UsersDetailsUpdate.as_view()),
    path('delete/<int:pk>', views.UsersDetailsDelete.as_view()),
]
admin.site.unregister(Association)
admin.site.unregister(Nonce)
admin.site.unregister(UserSocialAuth)
admin.site.unregister(Group)
admin.site.site_header = "Scholarship Dashboard"
admin.site.site_title = "Admin Dashboard"
admin.site.index_title = "Scholarship Dashboard"
