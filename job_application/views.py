# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils import timezone

from job_application.forms.job_form import CoverLetterForm
from job_application.models import JobApplication
from user.forms.profile_form import ContactInformationForm, ExperienceForm, ReferenceForm
from user.models import ContactInformation, Profile, Experience, Reference
from django.http import JsonResponse, HttpResponseRedirect

# Check if the job application has been submitted.
def check_submission_status(job_application):
    if job_application.status == 'submitted':
        return True
    return False

# Handle the contact information step of the job application process.
@login_required
def job_application_contact_info(request, job_id):
    profile = request.user.profile
    job_application, created = JobApplication.objects.get_or_create(
        user=request.user,
        job_id=job_id,
        defaults={'status': 'in_progress'}
    )
    request.session['job_application_id'] = job_application.id

    if check_submission_status(job_application):
        return redirect(reverse('job-details', args=[job_id]))

    contact_info = ContactInformation.objects.filter(job_application=job_application).first()

    if request.method == 'POST':
        form = ContactInformationForm(request.POST, instance=contact_info)
        if form.is_valid():
            contact_info = form.save(commit=False)
            contact_info.from_profile = False
            contact_info.profile = profile
            contact_info.job_application = job_application
            contact_info.save()
            return redirect('job_application_cover_letter', job_id=job_id)
    else:
        form = ContactInformationForm(instance=contact_info)

    return render(request, 'job_application/contact_info.html', {'form': form, 'job_application': job_application})

# Auto-fill the contact information form using data from the user's profile.
@login_required
def auto_fill_contact_info(request):
    profile = request.user.profile
    contact_info = ContactInformation.objects.filter(profile=profile, from_profile=True).first()

    if contact_info:
        data = {
            'success': True,
            'full_name': contact_info.full_name,
            'birthdate': contact_info.birthdate,
            'phone_number': contact_info.phone_number,
            'street_name': contact_info.street_name,
            'house_number': contact_info.house_number,
            'city': contact_info.city,
            'postal_code': contact_info.postal_code,
            'country': contact_info.country.code,
        }
    else:
        data = {'success': False}

    return JsonResponse(data)

# Handle the cover letter step of the job application process.
@login_required
def job_application_cover_letter(request, job_id):
    job_application = get_object_or_404(JobApplication, user=request.user, job_id=job_id)

    if check_submission_status(job_application):
        return redirect(reverse('job-details', args=[job_id]))

    if request.method == 'POST':
        form = CoverLetterForm(request.POST, instance=job_application)
        if form.is_valid():
            form.save()
            return redirect('job_application_experiences', job_id=job_id)
    else:
        form = CoverLetterForm(instance=job_application)

    return render(request, 'job_application/cover_letter.html', {'form': form, 'job_application': job_application})

# Display the experiences step of the job application process.
@login_required
def job_application_experiences(request, job_id):
    job_application = get_object_or_404(JobApplication, user=request.user, job_id=job_id)

    if check_submission_status(job_application):
        return redirect(reverse('job-details', args=[job_id]))

    experiences = Experience.objects.filter(job_application=job_application)

    form = ExperienceForm()
    return render(request, 'job_application/experiences.html', {
        'experiences': experiences,
        'form': form,
        'job_application': job_application
    })

# Add a new experience to the job application.
@login_required
def add_job_application_experience(request, job_id):
    job_application = get_object_or_404(JobApplication, user=request.user, job_id=job_id)
    profile = request.user.profile

    if check_submission_status(job_application):
        return redirect(reverse('job-details', args=[job_id]))

    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.job_application = job_application
            experience.profile = profile
            experience.from_profile = False
            experience.save()
            return redirect('job_application_experiences', job_id=job_id)

    return redirect('job_application_experiences', job_id=job_id)

# Delete an experience from the job application.
@login_required
def delete_job_application_experience(request, job_id, experience_id):
    experience = get_object_or_404(Experience, id=experience_id, job_application__user=request.user,
                                   job_application__job_id=job_id)

    if check_submission_status(experience.job_application):
        return redirect(reverse('job-details', args=[job_id]))

    if request.method == 'POST':
        experience.delete()
        return redirect('job_application_experiences', job_id=job_id)

    return render(request, 'job_application/delete_experience.html', {'experience': experience})

# Auto-fill the job application experiences using data from the user's profile.
@login_required
def auto_fill_job_application_experiences(request, job_id):
    profile = request.user.profile
    job_application = get_object_or_404(JobApplication, user=request.user, job_id=job_id)

    if check_submission_status(job_application):
        return redirect(reverse('job-details', args=[job_id]))

    profile_experiences = Experience.objects.filter(profile=profile, from_profile=True)

    for experience in profile_experiences:
        experience.pk = None
        experience.job_application = job_application
        experience.from_profile = False
        experience.save()

    return redirect('job_application_experiences', job_id=job_id)

# Display the references step of the job application process.
@login_required
def job_application_references(request, job_id):
    job_application = get_object_or_404(JobApplication, user=request.user, job_id=job_id)

    if check_submission_status(job_application):
        return redirect(reverse('job-details', args=[job_id]))

    references = Reference.objects.filter(job_application=job_application)

    form = ReferenceForm()
    return render(request, 'job_application/references.html', {
        'references': references,
        'form': form,
        'job_application': job_application
    })

# Add a new reference to the job application.
@login_required
def add_job_application_reference(request, job_id):
    job_application = get_object_or_404(JobApplication, user=request.user, job_id=job_id)
    profile = request.user.profile

    if check_submission_status(job_application):
        return redirect(reverse('job-details', args=[job_id]))

    if request.method == 'POST':
        form = ReferenceForm(request.POST)
        if form.is_valid():
            reference = form.save(commit=False)
            reference.job_application = job_application
            reference.profile = profile
            reference.from_profile = False
            reference.save()
            return redirect('job_application_references', job_id=job_id)

    return redirect('job_application_references', job_id=job_id)

# Delete a reference from the job application.
@login_required
def delete_job_application_reference(request, job_id, reference_id):
    reference = get_object_or_404(Reference, id=reference_id, job_application__user=request.user, job_application__job_id=job_id)

    if check_submission_status(reference.job_application):
        return redirect(reverse('job-details', args=[job_id]))

    if request.method == 'POST':
        reference.delete()
        return redirect('job_application_references', job_id=job_id)

    return render(request, 'job_application/delete_reference.html', {'reference': reference})

# Auto-fill the job application references using data from the user's profile.
@login_required
def auto_fill_job_application_references(request, job_id):
    profile = request.user.profile
    job_application = get_object_or_404(JobApplication, user=request.user, job_id=job_id)

    if check_submission_status(job_application):
        return redirect(reverse('job-details', args=[job_id]))

    profile_references = Reference.objects.filter(profile=profile, from_profile=True)

    for ref in profile_references:
        ref.pk = None
        ref.job_application = job_application
        ref.from_profile = False
        ref.save()

    return redirect('job_application_references', job_id=job_id)

# Display the review step of the job application process.
@login_required
def job_application_review(request, job_id):
    job_application = get_object_or_404(JobApplication, user=request.user, job_id=job_id)

    if check_submission_status(job_application):
        return HttpResponseRedirect(reverse('job-details', args=[job_id]))

    contact_info = ContactInformation.objects.filter(job_application=job_application).first()
    experiences = Experience.objects.filter(job_application=job_application)
    references = Reference.objects.filter(job_application=job_application)

    context = {
        'job_application': job_application,
        'contact_info': contact_info,
        'experiences': experiences,
        'references': references,
    }
    return render(request, 'job_application/review.html', context)

# Submit the job application.
@login_required
def submit_job_application(request, job_id):
    job_application = get_object_or_404(JobApplication, user=request.user, job_id=job_id)

    if request.method == 'POST':
        job_application.is_submitted = True
        job_application.submitted_at = timezone.now()
        job_application.status = 'submitted'
        job_application.save()
        return redirect('job_application_success', job_id=job_id)

    return redirect('job_application_review', job_id=job_id)

# Display the success page after submitting the job application.
@login_required
def job_application_success(request, job_id):
    job_application = get_object_or_404(JobApplication, user=request.user, job_id=job_id)

    if not job_application.is_submitted:
        return redirect('job_application_review', job_id=job_id)

    return render(request, 'job_application/success.html', {'job_id': job_id})

# Display the user's submitted job applications.
@login_required
def your_applications(request):
    user = request.user
    applications = JobApplication.objects.filter(user=user, status='submitted').order_by('-submitted_at')
    context = {'applications': applications}
    template_name = 'job_application/your_applications.html'
    return render(request, template_name, context)
