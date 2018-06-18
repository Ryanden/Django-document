from django.db import models

# Create your models here.


class Topping(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Pizza(models.Model):

    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(
        Topping,
        related_name='pizzas',
    )

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Group(models.Model):

    name = models.CharField(max_length=120)
    members = models.ManyToManyField(
        Person,
        through='Membership',
        through_fields=('group', 'person'),
    )

    def __str__(self):
        return self.name


class Membership(models.Model):

    person = models.ForeignKey(
        Person,
        related_name='memberships',
        on_delete=models.CASCADE
    )
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    recommender = models.ForeignKey(
        Person,
        related_name='memberships_by_recommender',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

    def __str__(self):
        return '{person} - {group} ({date})'.format(
            person=self.person.name,
            group=self.group.name,
            date=self.date_joined,
        )


