from django.urls import path
from . import views
from .views import AppListCreate, AppRetrieveUpdateDestroy

urlpatterns = [
    path('', views.signin, name='signin'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('admin', views.admin, name='admin'),
    path('apps/', AppListCreate.as_view(), name='app-list-create'),
    path('apps/<int:pk>/', AppRetrieveUpdateDestroy.as_view(), name='app-retrieve-update-destroy'),
]