from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to


urlpatterns = patterns('wbproject.views',
    # redirect root URL to wbinventory root URL
    url(regex=  r'^$',
        name=   'site_index',
        view=   'index',
    ),

    # mount wbinventory app at inventory/
    url(regex=  r'^wbinventory/',
        view=   include('wbinventory.urls'),
    ),
)
