from django.conf.urls.defaults import patterns, include, url
from wbproject.forms import AuthenticationForm


urlpatterns = patterns('',
    # redirect root URL to wbinventory root URL
    url(
        r'^$',
        'wbproject.views.index',
        name=   'site_index',
    ),

    # mount wbinventory app
    url(
        r'^wbinventory/',
        include('wbinventory.urls'),
        kwargs= dict(
            login_required=True,
        ),
    ),

    # authentication
    url(
        r'^accounts/login/$',
        'django.contrib.auth.views.login',
        name='accounts_login',
        kwargs=dict(
            authentication_form=AuthenticationForm,
        ),
    ),
    url(
        r'^accounts/logout/$',
        'django.contrib.auth.views.logout',
        name='accounts_logout',
        kwargs=dict(
            next_page='/',
        ),
    ),
)
