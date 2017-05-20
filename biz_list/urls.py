from django.conf.urls import url, include
from biz_list import views

app_name="biz"

urlpatterns = [
    url(r'^$',views.AboutView.as_view(), name="About"),
    url(r'^create/$',views.AboutCreate.as_view(), name="create"),
    url(r'^biznames/$',views.AboutListView.as_view(), name="biznames"),
    url(r'^biznames/(?P<pk>\d)/$', views.BizDetailView.as_view(),name="detail"),
]
