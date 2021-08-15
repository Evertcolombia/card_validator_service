from django.db import models

# Create your models here.
class CardNumber(models.Model):
    card_num = models.CharField(max_length=50, unique=True)
    supplier = models.CharField(max_length=50, blank=True, default='')
    save_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-save_at']
