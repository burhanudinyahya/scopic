from django.contrib.auth.models import AnonymousUser

class ServerUser(AnonymousUser):

    @property
    def is_authenticated(self):
        return True