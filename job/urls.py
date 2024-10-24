from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='job-index'),
    path('<int:id>', views.get_job_by_id, name='job-details'),
    path('post-job/<int:company_id>/', views.post_job, name='post-job'),
    path('<int:job_id>/delete/', views.delete_job, name='delete_job'),
    path('fetch-categories/', views.fetch_categories, name='fetch-categories'),
    path('fetch-companies/', views.fetch_companies, name='fetch-companies'),
    path('toggle-favorite/<int:job_id>/', views.toggle_favorite, name='toggle_favorite'),
]
