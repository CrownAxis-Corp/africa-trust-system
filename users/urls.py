from rest_framework.routers import DefaultRouter
from .views import UserViewSet, LoginView, RegisterView
from django.urls import path

router = DefaultRouter()

router.register(r'users', UserViewSet, basename='user')

urlpatterns = router.urls + [
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/register/', RegisterView.as_view(), name='register')
]