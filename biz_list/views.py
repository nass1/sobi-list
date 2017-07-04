from .filters import UserFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#=====================================
from django.template.defaulttags import register
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import SingleObjectMixin
from . forms import AboutForm, NameForm, CatoForm
from . models import About
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
class IndexView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['biznames'] = About.objects.all()[:5]
        return context


class DraftListView(LoginRequiredMixin,ListView):
    #login_url = '/login/'

    context_object_name = "posts"
    model = About
    template_name = 'biz_list/draft_list.html'
    redirect_field_name = 'biz_list/about_list.html'
    def get_queryset(self):
        return About.objects.filter(approved_published=False)


@login_required
def post_publish(request, pk):
    post = get_object_or_404(About, pk=pk)
    post.approve()
    return redirect('/drafts/', pk=pk)

class AboutCreate(CreateView):
    model = About
    success_url = '/success/'
    form_class = AboutForm



class SuccessUrl(TemplateView):
    template_name = 'biz_list/success_url.html'


class BizContact(TemplateView):
    template_name = 'biz_list/biz_contact.html'

'''
def get_name(request,nameid):
    # if this is a POST request we need to process the form data
    abc = request.path
    print ("the ree is ", abc)
    abc = About.objects.filter(category=nameid)
    return render(request, 'biz_list/about_list.html', {'biznames': abc})

'''


#######################################
"""
class SearchList(SingleObjectMixin, ListView):
    template_name = "biz_list/search.html"
    model = About
    context_object_name = "biznames"
    #queryset  = About.objects.filter(category__startswith="Restaurants")
"""





def search(request):
    user_list = About.objects.filter(approved_published=True)
    user_filter = UserFilter(request.GET, queryset=user_list).qs
    page = request.GET.get('page', 1)
    paginator = Paginator(user_filter, 4)

    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'biz_list/about_list.html', {'filter': user_filter, 'contacts': contacts})

#https://simpleisbetterthancomplex.com/tutorial/2016/11/28/how-to-filter-querysets-dynamically.html

######################### to be continued #############################

#######################################
"""
class AboutListView(FormMixin, ListView):
    context_object_name = "biznames"
    model = About #about_list.html
    form_class = CatoForm
    paginate_by = 10

"""

class BizDetailViewDraft(DetailView):
    context_object_name = 'biz_details'
    # 'models' is used to connect to databse
    model = About
    # template_name is required to view the the pages. like below
    template_name = 'biz_list/biz_detail_draft.html'

    def get_queryset(self):
        return About.objects.filter(approved_published=False)



class BizDetailView(DetailView):
    context_object_name = 'biz_details'
    # 'models' is used to connect to databse
    model = About
    # template_name is required to view the the pages. like below
    template_name = 'biz_list/biz_detail.html'

    def get_queryset(self):
        return About.objects.filter(approved_published=True)
