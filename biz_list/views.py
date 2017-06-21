from django.template.defaulttags import register
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import SingleObjectMixin
from . forms import AboutForm, NameForm
from . models import About
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)

from django.http import HttpRequest, HttpResponseRedirect, HttpResponse

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


def get_name(request, nameid):
    # if this is a POST request we need to process the form data
    abc = request.path
    print ("the ree is ", abc)
    abc = About.objects.filter(category=nameid)

    return render(request, 'biz_list/about_list.html', {'biznames': abc})

#######################################
"""
class SearchList(SingleObjectMixin, ListView):
    template_name = "biz_list/search.html"
    model = About
    context_object_name = "biznames"
    #queryset  = About.objects.filter(category__startswith="Restaurants")
"""








######################### to be continued #############################

#######################################

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
