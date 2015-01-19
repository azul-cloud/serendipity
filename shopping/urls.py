from django.conf.urls import url, patterns

from . import views


prefix = "shopping_"

urlpatterns = patterns('shopping.views',
    url(r'^add/(?P<pk>\d+)/$', views.AddView.as_view(), name=prefix + 'add'),
    url(r'^remove/(?P<pk>\d+)/$', views.RemoveView.as_view(), name=prefix + 'remove'),
    url(r'^removesingle/(?P<pk>\d+)/$', views.RemoveSingleView.as_view(), 
        name=prefix + 'remove_single'),
    url(r'^cart/$', views.CartTemplateView.as_view(), name=prefix + 'cart'),
    url(r'^charge/$', views.charge, name=prefix + 'charge'),
    
    url(r'^admin/sale/(?P<pk>\d+)/$', views.SaleDetailView.as_view(), 
        name=prefix + 'sale'),
    url(r'^admin/sales/$', views.SaleListView.as_view(), 
        name=prefix + 'sales'),
    url(r'^admin/sales/errors/$', views.SaleErrorListView.as_view(), 
        name=prefix + 'sale_errors'),
)