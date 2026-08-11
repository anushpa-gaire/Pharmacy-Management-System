from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import render
from apps.pharmacy.models import Pharmacy
from apps.pharmacy.form import PharmacyForm


class PharmacyListView(View):
    # for listing data
    def get(self, request):
        pharmacies = Pharmacy.objects.all()

        context = {"pharmacies": pharmacies}
        return render(request, "pharmacy/list.html", context)


# for create operations
class PharmacyCreateView(CreateView):
    model = Pharmacy
    form_class = PharmacyForm
    template_name = "pharmacy/create.html"
    success_url = reverse_lazy("pharmacy_list")


# for update operations
class PharmacyUpdateView(UpdateView):
    model = Pharmacy
    form_class = PharmacyForm
    template_name = "pharmacy/create.html"
    success_url = reverse_lazy("pharmacy_list")


# for delete operations
class PharmacyDeleteView(DeleteView):
    model = Pharmacy
    template_name = "pharmacy/delete.html"
    success_url = reverse_lazy("pharmacy_list")


# for detail operations
class PharmacyDetailView(DetailView):
    model = Pharmacy
    template_name = "pharmacy/detail.html"
    context_object_name = "pharmacy"