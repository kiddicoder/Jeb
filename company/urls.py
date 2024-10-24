from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='company-index'),
    path('create/', views.create_company, name='create-company'),
    path('<int:id>', views.get_company_by_id, name='company-details'),
    path('your-companies/', views.your_companies, name='your-companies'),
    path('<int:id>/delete/', views.delete_company, name='delete_company'),
    path('choose-company-for-job/', views.your_companies, {'for_job_posting': True}, name='choose-company-for-job'),
]
