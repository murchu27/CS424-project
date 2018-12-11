from rest_framework import serializers

from productions.models import Production

class ProductionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Production
        fields = ('name','description','date_time','price')

