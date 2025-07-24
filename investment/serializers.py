from .models import Transaction, UserInvestment, Wallet
from rest_framework.serializers import Serializer, ModelSerializer

class TransactionSerializer(ModelSerializer):

    class Meta:
        model = Transaction
        exclude = ['user']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        print(f'transaction made by:{user.get_full_name()}')
        validated_data['user'] = user
        return super().create(validated_data)


class WalletSerializer(ModelSerializer):

    class Meta:
        model = Wallet
        exclude = ['user']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        validated_data['user'] = user
        return super().create(validated_data)
    

