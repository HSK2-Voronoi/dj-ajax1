from django.urls import path
from . import views


urlpatterns = [
	path('', views.list_jobs, name='list_jobs'),
	path('api/get_jobs/', views.get_jobs),
	path('api/list_jobs/', views.list_jobs),
	path('api/list_jobs/<int:pk>/', views.detail_jobs),
	path('api/list_jobs/create/', views.create_jobs),
	path('api/list_jobs/<int:pk>/update', views.update_jobs),
] 

