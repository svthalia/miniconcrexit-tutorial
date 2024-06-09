from django.db import models


class Reimbursement(models.Model):
    owner = models.ForeignKey(
        "auth.User",
        related_name="reimbursements",
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_incurred = models.DateField()
    description = models.TextField()
    receipt = models.FileField(upload_to="receipts/")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    approved = models.BooleanField(default=False)
    approved_at = models.DateTimeField(null=True)
    approved_by = models.ForeignKey(
        "auth.User",
        related_name="reimbursements_approved",
        on_delete=models.SET_NULL,
        editable=False,
        null=True,
    )

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return f"Reimbursement #{self.id}"
