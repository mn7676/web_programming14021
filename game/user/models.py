from django.db import models

class test(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.CharField(max_length=11, default="09121765555", null=True)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"