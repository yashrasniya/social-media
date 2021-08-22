from rest_framework import authentication
from django.contrib.auth import get_user_model


class Authentication(authentication.BasicAuthentication):

    def authenticate(self, requst):
        print(requst.user)
        qs = get_user_model().objects.all()
        user = qs.order_by("id").first()
        return user, None
