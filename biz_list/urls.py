from django.conf.urls import url, include
from biz_list import views
from django.conf.urls.static import static
from django.conf import settings
from .filters import UserFilter
from . models import About

app_name="bizweb"

urlpatterns = [
    url(r'^$',views.IndexView.as_view(), name="mainpage"),
    url(r'^create/$',views.AboutCreate.as_view(), name="create"),
    url(r'^bizlist/$', views.search, name="bizlist"),

    url(r'^bizlist/(?P<pk>\d*)/$', views.BizDetailView.as_view(),name="detail"),
    #url(r'^search/([\w-]+)/$',views.SearchList.as_view(), name="search"),
    #url(r'^search/([\w-]+)/$',views.get_name, name="search"),
    #url(r'^filter/([\w-]*)/$',views.AboutListViewCountry.as_view, name="filter"),
    #url(r'^filter/$', views.search, name='filter'),
    url(r'^drafts/$', views.DraftListView.as_view(), name='post_draft_list'),
    url(r'^bizlist/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^ddrafts/(?P<pk>\d+)/$', views.BizDetailViewDraft.as_view(),name="ddrafts"),
    url(r'^success/$', views.SuccessUrl.as_view(), name='success'),
    url(r'^contact/$', views.BizContact.as_view(), name='contact'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
