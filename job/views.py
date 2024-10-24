from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse

from company.models import Company
from job.forms.job_form import JobForm
from job.models import Job, JobCategory, FavoriteJob
from job_application.models import JobApplication


# This function handles the display and filtering of job listings.
# Import the timezone module
from django.utils import timezone

# This function handles the display and filtering of job listings.
@login_required
def index(request):
    # Retrieve filter and sorting parameters from the request.
    search_filter = request.GET.get('search_filter', '')
    sort_by = request.GET.get('sort_by', 'date')
    category_filter = request.GET.get('categories', '')
    company_filter = request.GET.get('companies', '')
    applied_filter = request.GET.get('applied_filter', '')
    favorites_filter = request.GET.get('favorites_filter', '')

    # Convert filter parameters to lists of integers.
    category_filter_list = [int(id) for id in category_filter.split(',')] if category_filter else []
    company_filter_list = [int(id) for id in company_filter.split(',')] if company_filter else []

    # Determine the ordering of job listings based on the sort parameter.
    if sort_by == 'date':
        ordering = '-created_at'
    elif sort_by == 'due_date':
        ordering = 'due_date'
    else:
        ordering = 'title'

    # Get the current date to filter out due jobs.
    current_date = timezone.now().date()

    # Filter job listings based on the search and filter parameters, and exclude due jobs.
    jobs = Job.objects.filter(title__icontains=search_filter, due_date__gte=current_date).order_by(ordering)
    if category_filter_list:
        jobs = jobs.filter(category__id__in=category_filter_list)
    if company_filter_list:
        jobs = jobs.filter(company__id__in=company_filter_list)

    if applied_filter == 'applied':
        jobs = jobs.filter(applications__is_submitted=True, applications__user=request.user)
    elif applied_filter == 'not_applied':
        jobs = jobs.exclude(applications__is_submitted=True, applications__user=request.user)
    elif applied_filter == 'both':  # This case should return no results
        jobs = jobs.none()

    if favorites_filter == 'favorites':
        jobs = jobs.filter(favorited_by__user=request.user)

    favorite_job_ids = set(FavoriteJob.objects.filter(user=request.user).values_list('job_id', flat=True))

    # If the request is an AJAX request, return filtered jobs as JSON.
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        jobs_data = [{
            'id': x.id,
            'title': x.title,
            'created_at': x.created_at.isoformat(),
            'company_logo': x.company.logo.url,
            'company_name': x.company.name,
            'due_date': x.due_date.strftime('%b %d'),
            'is_favorited': x.id in favorite_job_ids
        } for x in jobs]

        return JsonResponse({'data': jobs_data})

    # Retrieve all categories and companies for filtering options.
    categories = JobCategory.objects.all()
    companies = Company.objects.all()
    context = {
        'jobs': jobs,
        'categories': categories,
        'selected_categories': category_filter_list,
        'companies': companies,
        'selected_companies': company_filter_list,
        'applied_filter': applied_filter,
        'favorites_filter': favorites_filter,
        'favorite_job_ids': favorite_job_ids,
    }
    return render(request, 'job/index.html', context)



# This function handles displaying the details of a specific job.
@login_required
def get_job_by_id(request, id):
    job = get_object_or_404(Job, pk=id)
    application = None
    if request.user.is_authenticated:
        application = JobApplication.objects.filter(job=job, user=request.user).first()

    context = {
        'job': job,
        'application': application,
    }
    return render(request, 'job/job_details.html', context)

# This function handles posting a new job for a specific company.
@login_required
def post_job(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.company = company
            job.location = company.address
            job.save()
            return redirect('job-index')
    else:
        form = JobForm()

    return render(request, 'job/post_job.html', {'form': form, 'company': company})


@login_required
def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, company__user=request.user)
    if request.method == 'POST':
        job.delete()
        return redirect('job-index')
    return redirect('job_detail', job_id=job.id)


@login_required
def toggle_favorite(request, job_id):
    job = Job.objects.get(id=job_id)
    favorite, created = FavoriteJob.objects.get_or_create(user=request.user, job=job)

    if not created:
        # If the favorite already exists, remove it
        favorite.delete()
        return JsonResponse({'status': 'removed'})

    return JsonResponse({'status': 'added'})


# This function retrieves all job categories and returns them as JSON.
def fetch_categories(request):
    categories = JobCategory.objects.all()
    categories_data = [{'id': category.id, 'name': category.name} for category in categories]
    return JsonResponse({'filters': categories_data})


# This function retrieves all companies and returns them as JSON.
def fetch_companies(request):
    companies = Company.objects.all()
    companies_data = [{'id': company.id, 'name': company.name} for company in companies]
    return JsonResponse({'filters': companies_data})
