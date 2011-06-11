from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


class LoginRequiredMiddleware(object):
    """
    Middleware to look for ``login_required`` keyword argument on URLs
    and present anonymous users with a login sequence.
    """

    def process_view(self, request, view_func, view_args, view_kwargs):
        login_required = view_kwargs.pop('login_required', False)
        if login_required:
            if not request.user.is_authenticated():
                url = '{0}?next={1}'.format(
                    reverse('accounts_login'),
                    request.META['PATH_INFO'],
                )
                return HttpResponseRedirect(url)
        else:
            return
