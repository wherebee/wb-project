from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to


urlpatterns = patterns('',
    # redirect root URL to inventory/
    url(regex=  r'^$',
        name=   'site_index',
        view=   redirect_to,
        kwargs= {
            'url': '/inventory/',
        },
    ),

    # mount wbinventory app at inventory/
    url(regex=  r'^wbinventory/',
        view=   include('wbinventory.urls'),
    ),
)
