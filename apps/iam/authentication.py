from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from apps.utilities.errors import Error, APIError
from apps.iam import models
from django.contrib.auth.models import Group
import requests
import keycloak

class CustomJWTAuthentication(JWTAuthentication):
    # ENTRY POINT OF AUTHENTICATION AT ANY REQUEST, regardless if it's authenticated or not. Below function will run anyway
    # @Override
    def authenticate(self, request):
        return self.authenticate_credentials(self.get_token(request))
    def authenticate_credentials(self, auth):
        auth_type = auth[0]
        token = auth[1]
        try:
            if token is None or token == '':
                return None
            # Verify JWT token against Keycloak IAM
            try:
                user_details = settings.KEYCLOAK_CLIENT.userinfo(token)
                user, created = models.User.objects.get_or_create(
                                            id=user_details.get('sub'),
                                        )
                update_user = models.User.objects.filter(id=user_details.get('sub')).update(
                                            username=user_details.get('preferred_username'),
                                            email=user_details.get('email'),
                                            first_name=user_details.get('given_name'),
                                            last_name=user_details.get('family_name'),
                                            is_email_verified=user_details.get('email_verified')
                                        )
            except keycloak.exceptions.KeycloakAuthenticationError as e:
                return None
            # update user group
            user_group = user_details.get('groups')
            try:
                for group in user_group:
                    if group == models.GroupEnum.ADMIN_GROUP.value:
                        sys_group = Group.objects.get(name=group)
                        user.groups.add(sys_group)
                        user.save()
                    elif group == models.GroupEnum.CUSTOMER_GROUP.value:
                        sys_group = Group.objects.get(name=group)
                        user.groups.add(sys_group)
                        user.save()
            except TypeError as e:
                raise APIError(Error.USER_GROUP_ERROR)
            # If the token is valid, return the user
            return user, token
        except requests.exceptions.HTTPError:
            # If the token is invalid, raise an exception
            raise AuthenticationFailed('Invalid token')
    def get_token(self, request) -> tuple:
        auth = request.META.get('HTTP_AUTHORIZATION')
        if auth is None:
            return None, ''
        auth_type, token = auth.split()
        return auth_type, token
