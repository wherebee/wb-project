from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('wbproject.views',
    url(regex=  r'^$',
        name=   'index',
        view=   'index',
    ),
)
