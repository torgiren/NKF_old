#-*- coding: utf-8 -*-
from django.db import models
# Create your models here.
class JM(models.Model):
	nazwa=models.CharField(max_length=10)
	def __unicode__(self):
		return u"%s"%self.nazwa 
	class Meta:
		ordering=['-nazwa']
class VAT(models.Model):
	wartosc=models.DecimalField(max_digits=3,decimal_places=0)
	def __unicode__(self):
		return u"%d"%self.wartosc
	class Meta:
		ordering=['-wartosc']
class Towar(models.Model):
	nazwa = models.CharField(max_length=30)
	jm=models.ForeignKey(JM,verbose_name='Jednostka miary')
#cena zakupu netto
	cena=models.DecimalField(max_digits=10,decimal_places=2,verbose_name='cena zak. netto')
	vat=models.ForeignKey(VAT,verbose_name='VAT')
	marza=models.DecimalField(max_digits=5,decimal_places=2,verbose_name=u'Marża(%)')
	kalkulacja=models.BooleanField()
	def __unicode__(self):
		return u"%s"%self.nazwa
	def __str__(self):
		return "Towar"
	def zakup_netto(self):
		return self.cena
	def zakup_brutto(self):
		return round(self.cena*(1+self.vat.wartosc/100),2)
	def sprzedaz_netto(self):
		return round(self.cena*(1+self.marza/100),2)
	def sprzedaz_brutto(self):
		return round(self.sprzedaz_netto()*(1.0+float(self.vat.wartosc)/float(100)),2)
	class Meta:
		ordering=['nazwa']


