from django.db import models

class CreateUpdateStatusAbstractModel(models.Model):
    ACTIVE = 1
    INACTIVE = 2
    DISABLED = 3
    DELETED = 4
    STATUS_CHOICES = (
        (ACTIVE, "active"),
        (INACTIVE, "inactive"),
        (DISABLED, "disabled"),
        (DELETED, "deleted")
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=ACTIVE)

    class Meta:
        abstract = True