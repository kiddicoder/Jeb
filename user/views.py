from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from user.forms.profile_form import ProfileForm, ContactInformationForm, ReferenceForm, ExperienceForm, \
    ProfilePictureForm
from user.models import Profile, ContactInformation, Reference, Experience

# Handle user registration.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            return redirect('login')
        else:
            context = {
                'form': form,
            }
            return render(request, 'user/register.html', context)

    context = {
        'form': UserCreationForm(),
    }
    return render(request, 'user/register.html', context)

# Display and update user profile information.
@login_required
def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    contact_info = None

    if profile:
        contact_info = ContactInformation.objects.filter(profile=profile, from_profile=True).first()

    if contact_info is None:
        contact_info_form = ContactInformationForm()
    else:
        contact_info_form = ContactInformationForm(instance=contact_info)

    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST, files=request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    reference_form = ReferenceForm()
    experience_form = ExperienceForm()

    experiences = Experience.objects.filter(profile=profile, from_profile=True)
    references = Reference.objects.filter(profile=profile, from_profile=True)

    context = {
        'form': form,
        'contact_info': contact_info,
        'contact_info_form': contact_info_form,
        'reference_form': reference_form,
        'experience_form': experience_form,
        'experiences': experiences,
        'references': references,
    }
    return render(request, 'user/profile.html', context)

# Update the user's profile picture.
@login_required
@require_POST
@csrf_exempt
def update_profile_picture(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfilePictureForm(request.POST, request.FILES, instance=profile)
    if form.is_valid():
        form.save()
        return JsonResponse({'profile_picture_url': profile.profile_picture.url})
    else:
        return JsonResponse({'error': 'Invalid form'}, status=400)

# Update the user's contact information.
@login_required
def update_contact_info(request):
    profile = Profile.objects.filter(user=request.user).first()
    contact_info, created = ContactInformation.objects.get_or_create(profile=profile, from_profile=True)

    if request.method == 'POST':
        form = ContactInformationForm(request.POST, instance=contact_info)

        if form.is_valid():
            form.save()
            return redirect(reverse('profile'))
        else:
            context = {
                'form': ProfileForm(instance=profile),
                'contact_info': contact_info,
                'contact_info_form': form,
                'errors': form.errors
            }
            return render(request, 'user/profile.html', context)

    return redirect(reverse('profile'))

# Add a new reference to the user's profile.
@login_required
def add_reference(request):
    profile = Profile.objects.filter(user=request.user).first()

    if request.method == 'POST':
        form = ReferenceForm(request.POST)

        if form.is_valid():
            reference = form.save(commit=False)
            reference.profile = profile
            reference.from_profile = True
            reference.save()
            return redirect(reverse('profile'))
        else:
            context = {
                'form': ProfileForm(instance=profile),
                'contact_info': ContactInformation.objects.filter(profile=profile, from_profile=True).first(),
                'contact_info_form': ContactInformationForm(instance=ContactInformation.objects.filter(profile=profile, from_profile=True).first()),
                'reference_form': form,
                'errors': form.errors,
            }
            return render(request, 'user/profile.html', context)

    return redirect(reverse('profile'))

# Delete a reference from the user's profile.
@login_required
def delete_reference(request, id):
    reference = get_object_or_404(Reference, pk=id, profile__user=request.user)

    if request.method == 'POST':
        reference.delete()
        return redirect('profile')

    return render(request, 'user/delete_reference.html', {'reference': reference})

# Add a new experience to the user's profile.
@login_required
def add_experience(request):
    profile = Profile.objects.filter(user=request.user).first()

    if request.method == 'POST':
        form = ExperienceForm(request.POST)

        if form.is_valid():
            experience = form.save(commit=False)
            experience.profile = profile
            experience.from_profile = True
            experience.save()
            return redirect(reverse('profile'))
        else:
            context = {
                'form': ProfileForm(instance=profile),
                'contact_info': ContactInformation.objects.filter(profile=profile, from_profile=True).first(),
                'contact_info_form': ContactInformationForm(instance=ContactInformation.objects.filter(profile=profile, from_profile=True).first()),
                'experience_form': form,
                'errors': form.errors,
            }
            return render(request, 'user/profile.html', context)

    return redirect(reverse('profile'))

# Delete an experience from the user's profile.
@login_required
def delete_experience(request, id):
    experience = get_object_or_404(Experience, pk=id, profile__user=request.user)

    if request.method == 'POST':
        experience.delete()
        return redirect('profile')

    return render(request, 'user/delete_experience.html', {'experience': experience})
