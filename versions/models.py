from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# from django.db.models import Model
# Create your models here.


class EntityRequirements(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class NetworkFulfillmentModels(models.Model):
    name = models.CharField(max_length=255)
    definition = models.CharField(max_length=255)
    entities_requirement = models.ManyToManyField(
        EntityRequirements, through='RequirementNetworkFulfillmentModel')

# method for updating


@receiver(post_save, sender=NetworkFulfillmentModels, dispatch_uid="update_stock_count")
def update_stock(sender, instance, **kwargs):
    # instance.product.stock -= instance.amount
    # instance.product.save()
    print(instance.entities_requirement, "111111111111111")


class RequirementNetworkFulfillmentModel(models.Model):
    entity_requirement = models.ForeignKey(
        EntityRequirements, on_delete=models.CASCADE)
    network_fulfillment_model = models.ForeignKey(
        NetworkFulfillmentModels, on_delete=models.CASCADE)
    version = models.CharField(max_length=255)  # ----
