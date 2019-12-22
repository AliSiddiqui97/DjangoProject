from rest_framework import routers
from .api import LeadViewSet

router = routers.DefaultRouter()
router.register('api', LeadViewSet, 'leads')

urlpatterns = router.urls