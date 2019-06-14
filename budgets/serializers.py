from rest_framework import serializers
from django.contrib.auth.models import User
from budgets.models import Bank, Account

class UserSerializer(serializers.HyperlinkedModelSerializer):
    accounts = serializers.HyperlinkedRelatedField(many=True, 
                                                   view_name='account-detail', 
                                                   read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'accounts')

class BankSerializer(serializers.HyperlinkedModelSerializer):
    accounts = serializers.HyperlinkedRelatedField(many=True,
                                                   view_name='account-detail', 
                                                   read_only=True)

    class Meta:
        model = Bank
        fields = ('name', 'logo_url', 'accounts')

class AccountSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Account
        fields = ('name', 'created_at', 'updated_at', 'bank')