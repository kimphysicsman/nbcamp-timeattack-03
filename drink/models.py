from django.db import models



class Category(models.Model):
    class Meta:
        db_table = "category"

    name = models.CharField(max_length=256)


class Drink(models.Model):
    class Meta:
        db_table = "drink"

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
