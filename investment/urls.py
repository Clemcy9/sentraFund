from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionsViewSet


router  = DefaultRouter()
router.register(r'transaction', TransactionsViewSet)

urlpatterns = [
    '', include(router.urls)
]