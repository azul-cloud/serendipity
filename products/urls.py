from django.conf.urls import patterns, include, url

from . import views


prefix = "product_"

urlpatterns = patterns('',
    url(r'admin/create/$', views.ProductCreateView.as_view(), name=prefix + "create"),
    url(r'admin/update/(?P<slug>\S+)/$', views.ProductUpdateView.as_view(), 
        name=prefix + "update"),
    url(r'admin/$', views.ProductAdminListView.as_view(), name=prefix + "admin_home"),
    
    url(r'type/(?P<slug>\S+)/$', views.ProductTypeDetailView.as_view(), name=prefix + "type"),
    url(r'$', views.ProductListView.as_view(), name=prefix + "home"),
    url(r'(?P<slug>\S+)/$', views.ProductDetailView.as_view(), name=prefix + "detail"),
)
