from django.db import models

# Create your models here.
__all__ = (
    'Place',
    'Restaurant',
    'Supplier'
)


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return f'[{self.pk}] Place({self.name})'


class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return f'[{self.pk}] Restaurant'


class Supplier(Place):

    # place_ptr = models.OneToOneField(
    #     Place, on_delete=models.CASCADE,
    #     parent_link=True,
    # )

    customer = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='supplier_by_customer'
    )
