from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'productions',views.ProductionViewSet)

urlpatterns = [
     path('production/id/<int:production_id>', views.production_detail, name='production_detail'),
     path('production/update/id/<int:production_id>', views.production_update, name='production_update'),
     path('productions', views.production_list, name='production_list'),
     path('restapi/',include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
