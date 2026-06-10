from rest_framework.routers import DefaultRouter
from .views import TrustViewSet

router = DefaultRouter()
router.register(r'trustevents', TrustViewSet, basename='trustevent')
urlpatterns = router.urls