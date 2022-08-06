from django.db import models

class Subscriber(models.Model):
	date = models.DateTimeField(auto_now = True)
	email = models.EmailField(max_length = 255)

	def __str__(self):
		return self.email



class Member(models.Model):
	legal_name = models.CharField(max_length = 255)
	chairman = models.CharField(max_length = 255)
	phone = models.CharField(max_length = 255)
	email = models.EmailField(max_length = 255)
	register_date = models.DateTimeField()
	certificate = models.CharField(max_length = 255)
	tin = models.CharField(max_length = 255)
	acsne = models.CharField(max_length = 255)
	activity = models.CharField(max_length = 255)
	capital_uzs = models.CharField(max_length = 255)
	capital_usd = models.CharField(max_length = 255)
	bank = models.CharField(max_length = 255)
	mfo = models.CharField(max_length = 255)
	founders = models.JSONField(default = list)

	legal_address_city = models.CharField(max_length = 255)
	legal_address_region = models.CharField(max_length = 255)
	legal_address_details = models.CharField(max_length = 255)
	legal_phone = models.CharField(max_length = 255)
	legal_fax = models.CharField(max_length = 255)
	legal_website = models.CharField(max_length = 255)

	production_address_city = models.CharField(max_length = 255)
	production_address_region = models.CharField(max_length = 255)
	production_address_details = models.CharField(max_length = 255)

	production_activity = models.CharField(max_length = 255)
	production_activity_details = models.CharField(max_length = 255)
	production_activity_products = models.CharField(max_length = 255)
	production_volume = models.CharField(max_length = 255)
	production_capacity = models.CharField(max_length = 255)
	production_operating_capacity = models.CharField(max_length = 255)
	production_workers_amount = models.CharField(max_length = 255)
	production_export = models.CharField(max_length = 255)
	production_products_volume_uzs = models.CharField(max_length = 255)
	production_products_volume_usd = models.CharField(max_length = 255)
	production_markets = models.CharField(max_length = 255)

	charter = models.FileField(upload_to = 'static/charters')



	def __str__(self):
		return self.legal_name