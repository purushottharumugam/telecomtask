from django.views.generic import ListView, DetailView, CreateView, UpdateView, \
    DeleteView
from .forms import CustomerForm
from .models import Customer, Plan
from django.urls import reverse_lazy


class CustomerListView(ListView):
    model = Customer
    template_name = 'customers.html'
    context_object_name = 'customers'

    def get_queryset(self):
        return Customer.objects.select_related('plan')


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer_details.html'
    context_object_name = 'customer'


class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'add_customer.html'
    form_class = CustomerForm
    success_url = reverse_lazy('customer_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['plan'].queryset = Plan.objects.all()
        return form


class RenewPlanView(UpdateView):
    model = Customer
    template_name = 'renew_plan.html'
    form_class = CustomerForm
    success_url = reverse_lazy('customer_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['plan'].queryset = Plan.objects.all()
        return form
