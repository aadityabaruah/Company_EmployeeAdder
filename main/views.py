from django.shortcuts import render, redirect
from main.models import Employee, Company
from django.views.generic import ListView

def add_employee(request, company_id):
    company = Company.objects.get(id=company_id)
    if request.method == 'POST':
        employee_id = request.POST.get('employee')
        employee = Employee.objects.get(id=employee_id)
        if not employee.company:
            employee.company = company
            employee.save()
        return redirect('companies')

    employees = Employee.objects.filter(company__isnull=True)
    context = {'company': company, 'employees': employees}
    return render(request, 'add_employee.html', context)

class CompanyListView(ListView):
    model = Company
    template_name = 'company_list.html'
    context_object_name = 'companies'

def companies_view(request):
    companies = Company.objects.all()
    context = {'companies': companies}
    return render(request, 'companies.html', context)
