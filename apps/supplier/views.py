from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from apps.supplier.models import Supplier
from apps.supplier.form import SupplierForm
from django.urls import reverse_lazy


# Create your views here.
# ListView
class SupplierList(ListView):
    model = Supplier
    template_name = "supplier/list.html"


# CreateView
class SupplierCreate(CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = "supplier/create.html"
    success_url = reverse_lazy("supplier_list")


# UpdateView
class SupplierUpdate(UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = "supplier/create.html"
    success_url = reverse_lazy("supplier_list")


# DeleteView
class SupplierDelete(DeleteView):
    model = Supplier
    template_name = "supplier/delete.html"
    success_url = reverse_lazy("supplier_list")


# DetailView
class SupplierDetail(DetailView):
    model = Supplier
    template_name = "supplier/Detail.html"