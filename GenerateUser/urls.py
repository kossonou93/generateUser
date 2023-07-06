from django.contrib import admin
from django.urls import path
from appuser import views as users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/add/<int:nbre>/', users.createUser),
    path('user/list/', users.listUser),
]
