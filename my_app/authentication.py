from rest_framework import authentication
from django.utils.translation import gettext_lazy as _
from .serveruser import ServerUser
from django.conf import settings

class BearerAuthentication(authentication.TokenAuthentication):
    keyword = 'Bearer'

    def authenticate(self, request):
        auth = authentication.get_authorization_header(request).split()

        if request.method != 'DELETE':
            return None

        if not auth:
            msg= _('Authentication credentials were not provided.')
            raise authentication.exceptions.NotAuthenticated(detail=msg, code=401)
        
        if auth[0].lower() != self.keyword.lower().encode():
            msg= _('Invalid token header.')
            raise authentication.exceptions.AuthenticationFailed(msg)

        if len(auth) == 1:
            msg = _('Invalid token header. No credentials provided.')
            raise authentication.exceptions.AuthenticationFailed(msg)

        elif len(auth) > 2:
            msg = _('Invalid token header. Token string should not contain spaces.')
            raise authentication.exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1].decode()
        except UnicodeError:
            msg = _('Invalid token header. Token string should not contain invalid characters.')
            raise authentication.exceptions.AuthenticationFailed(msg)

        if not (settings.CUSTOM_SERVER_AUTH_TOKEN == token):
            msg = _('You do not have permission to access this resource')
            raise authentication.exceptions.AuthenticationFailed(msg)

        user = ServerUser()

        return user, None