from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.ProjectListView.as_view(), name='project-list'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
    path('roles/', views.RoleListCreateView.as_view(), name='role-list'),
    path('permissions/', views.PermissionListCreateView.as_view(), name='permission-list'),
]
