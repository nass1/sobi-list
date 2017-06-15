from django.template.defaulttags import register
from django.shortcuts import render
from . forms import AboutForm
from . models import About
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)



class IndexView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['biznames'] = About.objects.all()[:5]
        return context

class AboutCreate(CreateView):
    model = About
    success_url = '/'
    fields = '__all__'




class AboutListView(ListView):
    context_object_name = "biznames"
    model = About
    #about_list.html




class BizDetailView(DetailView):
    context_object_name = 'biz_details'
    # 'models' is used to connect to databse
    model = About
    # template_name is required to view the the pages. like below
    template_name = 'biz_list/biz_detail.html'
