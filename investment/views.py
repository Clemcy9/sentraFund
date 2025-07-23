from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Transaction
from .serializers import TransactionSerializer


class TransactionsViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # return super().get_queryset()
        user = self.request.user
        if user.is_superuser:
            return self.queryset #all transactions if admin view
        return self.queryset.filter(user = user) #only return user's own transaction for regular user
    
    def perform_create(self, serializer):
        # return super().perform_create(serializer)
        serializer.save(user=self.request.user)
