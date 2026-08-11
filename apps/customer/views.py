from django.shortcuts import render

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from apps.customer.models import Customer
from apps.customer.form import CustomerForm

# Create your views here.

class CustomerListView(View):
    def get(self, request):
        customers = Customer.objects.all()

        context = {"customers": customers}
        return render(request, "customer/list.html", context)


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customer/create.html"
    success_url = reverse_lazy("customer_list")


class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customer/create.html"
    success_url = reverse_lazy("customer_list")


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = "customer/delete.html"
    success_url = reverse_lazy("customer_list")


class CustomerDetailView(DetailView):
    model = Customer
    template_name = "customer/detail.html"
    context_object_name = "customer"