from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Lead, Agent
from .forms import LeadModelForm

# Create your views here.


class LandingPageView(TemplateView):
    template_name = "landing.html"


# def landing_page(request):
#     return render(request, "landing.html")


class LeadListView(ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    # default name of queryset is object_list
    context_object_name = "leads"


# def lead_list(request):
#     leads = Lead.objects.all()
#     context = {"leads": leads}
#     # return HttpResponse("Hello World!")
#     return render(request, "leads/lead_list.html", context)


class LeadDetailView(DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    # default name of queryset is object_list
    context_object_name = "lead"


# def lead_detail(request, pk):
#     lead = Lead.objects.get(id=pk)
#     context = {"lead": lead}
#     return render(request, "leads/lead_detail.html", context)


class LeadCreateView(CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")


# def lead_create(request):
#     form = LeadModelForm()
#     # validar si el metodo es POST
#     if request.method == "POST":
#         print("Receiving a post request")
#         form = LeadModelForm(request.POST)
#         # validación del formulario
#         if form.is_valid():
#             form.save()
#             return redirect("/leads")
#     context = {"form": form}
#     return render(request, "leads/lead_create.html", context)


class LeadUpdateView(UpdateView):
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")


def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")

    context = {"lead": lead, "form": form}
    return render(request, "leads/lead_update.html", context)


def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")
