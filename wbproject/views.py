from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


def index(request):
    # Redirect to the web app's static HTML page.
    url = reverse('wbinventory_index')
    return HttpResponseRedirect(url)
