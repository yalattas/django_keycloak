from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import CustomerProfileAccess
from rest_framework import status
from .services import AccountService
from django.conf import settings
from django.http import HttpResponseRedirect
# Create your views here.

class KeycloakView(APIView):
    def get(self, request):
        # client = request.META['HOST_URL']
        client = "https://oauth.pstmn.io/v1/callback"
        auth_url = settings.KEYCLOAK_CLIENT.auth_url(
            # must whitelist front-end uri
            redirect_uri=client,
            scope="email",
            state=AccountService.generate_session_state(client)
        )
        return HttpResponseRedirect(redirect_to=auth_url)
class KeycloakAccessView(APIView):
    def post(self, request):
        # client = request.META['HOST_URL']
        client = "https://oauth.pstmn.io/v1/callback"
        access_response = settings.KEYCLOAK_CLIENT.token(
            grant_type='authorization_code',
            code=request.data['code'],
            redirect_uri=client
        )
        # token_type = access_response['token_type'] # should be Bearer
        access_token = access_response['access_token']
        return Response({"access_token":access_token}, status=status.HTTP_200_OK)

class TestView(APIView):
    permission_classes = [IsAuthenticated, CustomerProfileAccess]
    def get(self, request):
        return Response({'data':1})