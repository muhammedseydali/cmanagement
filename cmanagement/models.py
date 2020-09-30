from django.db import models

# Create your models here.
class category(models.Model):
	categories=models.CharField(null=True,max_length=100)

class items(models.Model):
	categoryy = models.CharField(null=True,max_length=100)
	item=models.CharField(max_length=100,null=True)

class vendor(models.Model):
	name=models.CharField(max_length=100)
	compony=models.CharField(max_length=100)
	email=models.EmailField()
	phone=models.CharField(max_length=15)
	remark=models.CharField(max_length=100)
	description=models.CharField(max_length=1025)

class locationn(models.Model):
	location=models.CharField(max_length=100)

class inventory(models.Model):
	category=models.CharField(max_length=100)
	locations=models.CharField(max_length=100)
	item=models.CharField(max_length=50)
	manufacture=models.CharField(max_length=100)
	serial_number=models.CharField(max_length=100)
	purchase_date=models.CharField(max_length=100)
	vendor=models.CharField(max_length=100)
	warranty=models.CharField(max_length=100)
	quantity=models.CharField(max_length=100)
	cost=models.CharField(max_length=100)
	total=models.CharField(max_length=100)
