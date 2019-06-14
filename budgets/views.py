from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from .serializers import UserSerializer, BankSerializer, AccountSerializer
from .models import Bank, Account
from .permissions import IsOwnerOrReadOnly

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This view set provides `list ` and `details` actions.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

class BankViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This view set provides `list ` and `details` actions.
    """

    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class AccountViewSet(viewsets.ModelViewSet):
    """
    This view set provides `list ` and `details` actions.
    """

    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, 
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
