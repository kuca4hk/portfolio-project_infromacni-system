from django.db.models.signals import pre_save
from django.dispatch import receiver
from ..apps.organizations.models import Organization
from ..apps.scholl_class.models import Class, Student, StudentDetail, StudyField
from import_export.signals import post_import, post_export


@receiver(pre_save, sender=Organization)
def set_pk_before_save(sender, instance, **kwargs):
    if not instance.dataOperationId or instance.uniqueCodeCategoryId:
        instance.dataOperationId = instance.pk
        instance.uniqueCodeCategoryId = instance.pk


@receiver(post_export, sender=StudentDetail)
def _post_export(model, **kwargs):
    if "full" in model:
        inner_data = model.pop("full")
        model.update(inner_data)
