from rest_framework import serializers
from .models import EntityRequirements, NetworkFulfillmentModels, RequirementNetworkFulfillmentModel


class EntityRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntityRequirements
        fields = ['id', 'name', 'description']


class NetworkFulfillmentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkFulfillmentModels
        fields = ['id', 'name', 'description', 'entities_requirement']


class RequirementNetworkFulfillmentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequirementNetworkFulfillmentModel
        fields = ['entity_requirement', 'network_fulfillment_model', 'version']
