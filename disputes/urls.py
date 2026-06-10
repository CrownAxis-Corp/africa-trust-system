from rest_framework.routers import DefaultRouter
from .views import DisputeViewset


router = DefaultRouter()
router.register(r'disputes',DisputeViewset, basename='dispute')
urlpatterns = router.urls