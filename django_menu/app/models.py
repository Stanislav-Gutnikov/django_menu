from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=50)
    parent_obj = models.ForeignKey(
        'Menu',
        null=True,
        blank=True,
        related_name='child_obj',
        on_delete=models.CASCADE
        )
    url = models.CharField(max_length=250)
    named_url = models.CharField(
        max_length=100,
        null=True,
        blank=True
        )

    def __str__(self):
        return self.name
