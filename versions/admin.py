from django.contrib import admin
from .models import EntityRequirements, NetworkFulfillmentModels, RequirementNetworkFulfillmentModel


# Register your models here.

admin.site.register([EntityRequirements, NetworkFulfillmentModels,
                    RequirementNetworkFulfillmentModel])
