from datetime import datetime, timedelta
from django.db import models
from django.conf import settings


class Pass(models.Model):

    price = models.IntegerField(verbose_name="Price")
    month_to_expire = models.IntegerField(verbose_name="Expires after x*30 days")
    date_released = models.DateTimeField(auto_now=True, verbose_name="Date Released")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="User",
        related_name="passes"
    )
    staff_who_released = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(value=None),
        verbose_name="StaffUser",
        related_name="passes_released"
    )

    def pass_is_expired(self) -> bool:
        date = self.date_released
        month = self.month_to_expire
        return datetime.now() >= date.to_python(date) + timedelta(days=(month.to_python(month) * 31))


class Product(models.Model):

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=2048)
    manufacturer = models.CharField(max_length=255)
    price = models.IntegerField()
    amount = models.IntegerField()
    image = models.ImageField(upload_to='products/', blank=True, null=True, default=None)

    def product_available(self):
        return self.amount.to_python(self.amount) > 0
