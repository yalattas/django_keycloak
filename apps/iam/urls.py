from django.urls import path

from . import views

urlpatterns = [
    path('keycloak/', views.KeycloakView.as_view(), name='keycloak'),
    path('keycloak/access/', views.KeycloakAccessView.as_view(), name='keycloak_token'),
    path('test/', views.TestView.as_view(), name='test')
]
