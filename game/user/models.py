from django.db import models


class Address(models.Model):
  st = models.CharField(max_length=50)

class test(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.CharField(max_length=11, default="09121765555", null=True)
  address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"