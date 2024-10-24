from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.utils import timezone

from company.forms.forms import CompanyForm
from company.models import Company
from job.models import Job, FavoriteJob


# This function renders a list of companies, and if a search filter is applied,
# it returns a filtered list of companies in JSON format.
def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        companies = [{
            'id': c.id,
            'name': c.name,
            'logo_url': c.logo.url,
        } for c in Company.objects.filter(name__icontains=search_filter)]

        return JsonResponse({'data': companies})

    context = {'companies': Company.objects.all().order_by('name')}
    return render(request, 'company/index.html', context)

# This function retrieves a specific company by its ID,
# along with the jobs associated with it, and renders the
# company details page. User must be logged in.
@login_required
def get_company_by_id(request, id):
    company = get_object_or_404(Company, pk=id)
    current_date = timezone.now().date()
    jobs = Job.objects.filter(company=company, due_date__gte=current_date).order_by('-created_at')
    favorite_job_ids = set(FavoriteJob.objects.filter(user=request.user).values_list('job_id', flat=True))
    context = {
        'company': company,
        'jobs': jobs,
        'favorite_job_ids': favorite_job_ids,
        'user': request.user
    }
    return render(request, 'company/company_details.html', context)


# This function retrieves all companies associated
# with the logged-in user and renders the
# appropriate template, either for job posting or for managing companies.
@login_required
def your_companies(request, for_job_posting=False):
    user = request.user
    companies = Company.objects.filter(user=user).order_by('name')
    context = {'companies': companies, 'for_job_posting': for_job_posting}
    template_name = 'company/choose_company_for_job.html' if for_job_posting else 'company/your_companies.html'
    return render(request, template_name, context)

# This function handles the creation of a new company.
# It processes the form data submitted via POST
# request, saves the company if the form is valid,
# and renders the creation form.
@login_required
def create_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            company = form.save(commit=False)
            company.user = request.user
            company.save()
            return redirect('your-companies')
    else:
        form = CompanyForm()

    return render(request, 'company/create_company.html', {'form': form})

# This function handles the deletion of a company.
# It verifies if the logged-in user owns the company
# before deleting it and redirects accordingly.
@login_required
def delete_company(request, id):
    company = get_object_or_404(Company, pk=id)
    if company.user == request.user:
        company.delete()
        return redirect('your-companies')
    else:
        return redirect('company-details', id=id)
