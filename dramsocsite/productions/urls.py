from . import views
from django.urls import path

urlpatterns = [
     path('production/id/<int:production_id>', views.production_detail),
     path('productions', views.production_list),
]
