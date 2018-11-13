from . import views
from django.urls import path

urlpatterns = [
     path('production/id/<int:production_id>', views.production_detail, name='production_detail'),
     path('production/update/id/<int:production_id>', views.production_update, name='production_update'),
     path('productions', views.production_list, name='production_list'),
]
