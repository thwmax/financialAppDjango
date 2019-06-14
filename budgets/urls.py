from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from budgets import views

router = DefaultRouter()
router.register(r'accounts', views.AccountViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'banks', views.BankViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]