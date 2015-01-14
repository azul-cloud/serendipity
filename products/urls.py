from django.conf.urls import patterns, include, url

from . import views


prefix = "product_"

urlpatterns = patterns('',
    url(r'create/$', views.ProductCreateView.as_view(), name=prefix + "create"),
    url(r'update/(?P<slug>\S+)/$', views.ProductUpdateView.as_view(), name=prefix + "update"),
    url(r'delete/(?P<slug>\S+)/$', views.ProductDeleteView.as_view(), name=prefix + "delete"),
    url(r'(?P<slug>\S+)/$', views.ProductDetailView.as_view(), name=prefix + "detail"),
    url(r'$', views.ProductHomeListView.as_view(), name=prefix + "home"),
)
