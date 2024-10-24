from django.urls import path
from job_application import views

urlpatterns = [
    path('<int:job_id>/contact-info/', views.job_application_contact_info, name='job_application_contact_info'),
    path('<int:job_id>/cover-letter/', views.job_application_cover_letter, name='job_application_cover_letter'),
    path('auto-fill-contact-info/', views.auto_fill_contact_info, name='auto_fill_contact_info'),
    path('<int:job_id>/experiences/', views.job_application_experiences, name='job_application_experiences'),
    path('<int:job_id>/experiences/add/', views.add_job_application_experience, name='add_job_application_experience'),
    path('<int:job_id>/experiences/<int:experience_id>/delete/', views.delete_job_application_experience, name='delete_job_application_experience'),
    path('<int:job_id>/auto-fill-experiences/', views.auto_fill_job_application_experiences, name='auto_fill_job_application_experiences'),
    path('<int:job_id>/references/', views.job_application_references, name='job_application_references'),
    path('<int:job_id>/references/add/', views.add_job_application_reference, name='add_job_application_reference'),
    path('<int:job_id>/references/<int:reference_id>/delete/', views.delete_job_application_reference, name='delete_job_application_reference'),
    path('<int:job_id>/auto-fill-references/', views.auto_fill_job_application_references, name='auto_fill_job_application_references'),
    path('<int:job_id>/review/', views.job_application_review, name='job_application_review'),
    path('<int:job_id>/submit/', views.submit_job_application, name='submit_job_application'),
    path('<int:job_id>/success/', views.job_application_success, name='job_application_success'),
    path('your-applications/', views.your_applications, name='your_applications'),
]
