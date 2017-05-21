from django.conf.urls import url, include
from biz_list import views
from django.conf.urls.static import static
from django.conf import settings
app_name="bizweb"

urlpatterns = [
    url(r'^$',views.IndexView.as_view(), name="mainpage"),
    url(r'^create/$',views.AboutCreate.as_view(), name="create"),
    url(r'^bizlist/$',views.AboutListView.as_view(), name="bizlist"),
    url(r'^bizlist/(?P<pk>\d*)/$', views.BizDetailView.as_view(),name="detail"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
