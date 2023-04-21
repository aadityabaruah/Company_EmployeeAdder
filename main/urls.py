from django.urls import path
from main.views import companies_view, add_employee, CompanyListView

app_name = 'api'

urlpatterns = [
    path('', companies_view, name='index'),
    path('companies/', companies_view, name='companies'),
    path('company_list/', CompanyListView.as_view(), name='company_list'),
    path('add_employee/<int:company_id>/', add_employee, name='add_employee'),
]
