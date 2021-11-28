from .views import *

from django.urls import path
from django.contrib.auth.views import LogoutView

from base import views as contact_views

urlpatterns = [
    path('home/', home_view, name='home'),
    path('aboutus/', about_view, name='aboutus'),
    path('site/', site_view, name='site'),
    path('checklist/', checklist_view, name='checklist'),
    path('contact/', contact_views.contact_view, name='contact'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', ListOfTask.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create-task/', CreateATask.as_view(), name='task-create'),
    path('task-change/<int:pk>/', UpdateTheTask.as_view(), name='task-update'),
    path('delete-task/<int:pk>/', DeleteATask.as_view(), name='task-delete'),
]
