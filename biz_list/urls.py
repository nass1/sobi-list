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
    url(r'^search/([\w-]+)/$',views.get_name, name="search"),
    #url(r'^filter/([\w-]*)/$',views.AboutListViewCountry.as_view, name="filter"),
    #url(r'^filter/$', views.search, name='filter'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
