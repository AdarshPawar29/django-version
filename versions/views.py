from django.http import JsonResponse
from .models import EntityRequirements, NetworkFulfillmentModels, RequirementNetworkFulfillmentModel
from .serializer import EntityRequirementSerializer, NetworkFulfillmentModelSerializer, RequirementNetworkFulfillmentModelSerializer

# get data
# serialize them
# return them as a json


def entity_requirement_list(request):
    entity_requirement = EntityRequirements.objects.all()
    serializer = EntityRequirementSerializer(entity_requirement, many=True)
    return JsonResponse({"entity_requirement": serializer.data}, safe=False)


def network_fulfillment_list(request):
    network_fulfillment = NetworkFulfillmentModels.objects.all()
    serializer = NetworkFulfillmentModelSerializer(
        network_fulfillment, many=True)
    return JsonResponse({"network_fulfillment": serializer.data}, safe=False)


def requirement_network_fulfillment_list(request):
    requirement_network_fulfillment = RequirementNetworkFulfillmentModel.objects.all()
    serializer = RequirementNetworkFulfillmentModelSerializer(
        requirement_network_fulfillment, many=True)
    return JsonResponse({"requirement_network_fulfillment": serializer.data})
