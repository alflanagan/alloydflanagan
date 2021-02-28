from rest_framework import serializers
from portfolios.models import Portfolio


class PortfolioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Portfolio
        fields = [
            'title', 'sub_title', 'body', 'main_image', 'thumb_image',
            'created', 'updated', 'position'
        ]
