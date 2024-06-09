from django.contrib import admin
from django.contrib.admin import register
from django.utils import timezone
from reimbursements import models


@register(models.Reimbursement)
class ReimbursementAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created",
        "owner",
        "date_incurred",
        "amount",
        "approved",
    )
    list_filter = ("approved", "created", "date_incurred", "owner")

    autocomplete_fields = ["owner"]
    readonly_fields = ["approved_by", "approved_at", "created", "updated"]

    def save_model(self, request, obj, form, change):
        if obj.approved and not form.initial["approved"]:
            obj.approved = True
            obj.approved_by = request.user
            obj.approved_at = timezone.now()

        super().save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.approved:
            return self.readonly_fields + [
                "approved",
                "amount",
                "description",
                "receipt",
                "date_incurred",
                "owner",
            ]
        return self.readonly_fields
