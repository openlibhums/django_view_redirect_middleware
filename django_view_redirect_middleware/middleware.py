from django.shortcuts import redirect
from django.urls import resolve, reverse, NoReverseMatch
from django.conf import settings


class ViewRedirectMiddleware:
    """
    Middleware to redirect requests based on the current view name for non-staff users.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.redirect_views = getattr(settings, 'REDIRECT_VIEWS', [])
        self.redirect_url = getattr(settings, 'REDIRECT_URL_NAME', None)


    def __call__(self, request):
        if request.user.is_authenticated and not request.user.is_staff:
            current_view = resolve(request.path_info).view_name

            if current_view in self.redirect_views:
                try:
                    redirect_url = reverse(self.redirect_url)
                except NoReverseMatch:
                    redirect_url = self.redirect_url

                return redirect(redirect_url)

        response = self.get_response(request)
        return response

