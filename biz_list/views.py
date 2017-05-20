from django.shortcuts import render
from . forms import AboutForm
from . models import About
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)

class AboutView(TemplateView):
    template_name = "about.html"


class AboutCreate(CreateView):
    model = About
    success_url = '/biz/'
    fields = '__all__'


class AboutListView(ListView):
    context_object_name = "biznames"
    model = About




class BizDetailView(DetailView):
    context_object_name = 'biz_details'
    # 'models' is used to connect to databse
    model = About
    # template_name is required to view the the pages. like below
    template_name = 'biz_list/biz_detail.html'
