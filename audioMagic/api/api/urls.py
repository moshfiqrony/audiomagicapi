from rest_framework.routers import DefaultRouter
from .views import MagicView

router = DefaultRouter()
router.register(r'audioMagic', MagicView, base_name='AudioMagicViews')

urlpatterns = router.urls