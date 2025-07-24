from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionsViewSet, WalletViewSet


router  = DefaultRouter()
router.register(r'transaction', TransactionsViewSet)
router.register(r'wallet', WalletViewSet)


urlpatterns = [
    path('', include(router.urls))
]