from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to
from wbproject.forms import AuthenticationForm


urlpatterns = patterns('',
    # redirect root URL to wbinventory root URL
    url(
        regex=  r'^$',
        name=   'site_index',
        view=   'wbproject.views.index',
    ),

    # mount wbinventory app
    url(
        regex=  r'^wbinventory/',
        view=   include('wbinventory.urls'),
        kwargs= dict(
            login_required=True,
        ),
    ),

    # authentication
    url(
        regex=  r'^accounts/login/$',
        name=   'accounts_login',
        view=   'django.contrib.auth.views.login',
        kwargs= dict(
            authentication_form=AuthenticationForm,
        ),
    ),
    url(
        regex=  r'^accounts/logout/$',
        name=   'accounts_logout',
        view=   'django.contrib.auth.views.logout',
        kwargs= dict(
            next_page='/',
        ),
    ),
)
