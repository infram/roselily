
# Create your models here.
from __future__ import unicode_literals
from django.db import models
from datetime import datetime





class Obrands(models.Model):

    Obrand_name = models.CharField(max_length = 25 ,verbose_name="Brand")

    Obrand_date = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Brand"

    def __str__(self):
        return self.Obrand_name


class Ocatergory(models.Model):
    verbose_name = "Catergory"
    Ocat_name = models.CharField(max_length=60, verbose_name="Catergory")
    Ocat_date = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "Catergory"

    def __str__(self):
        return self.Ocat_name


class Ocountry(models.Model):
    ocountry = models.CharField(max_length=50, verbose_name="Country")
    ocountrydate = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "Country"

    def __str__(self):
        return self.ocountry


class Oshop(models.Model):
    oshop_name = models.CharField(max_length=50, verbose_name="Shop Name")
    oshp_address = models.CharField(max_length=50, verbose_name="Address")
    oshp_phone = models.CharField(max_length=50, verbose_name="Phone")
    oshp_person = models.CharField(max_length=50, verbose_name="Contact Person")
    oshp_web = models.CharField(max_length=50, verbose_name="Www")
    oshp_email = models.EmailField(max_length=240, verbose_name="Email")
    oshp_locations = models.CharField(max_length=90, verbose_name="Location")

    class Meta:
        verbose_name = "Shop"

    def __str__(self):
        return self.oshop_name


class Opacking(models.Model):
    opacking_type = models.CharField(max_length=45, verbose_name="Packing")

    class Meta:
        verbose_name = "Packing"

    def __str__(self):
        return self.opacking_type


class Osubcatergory(models.Model):
    ocatergory = models.ForeignKey(Ocatergory, on_delete=models.CASCADE)
    osubcat = models.CharField(max_length=50, verbose_name="Sub Catergory")

    class Meta:
        verbose_name = "Sub Catergory"

    def __str__(self):
        return self.osubcat


class Oproducts(models.Model):
    pd_name = models.CharField(max_length=250, verbose_name="Name")
    pd_catid = models.ForeignKey(Ocatergory, on_delete=models.CASCADE, verbose_name="Catergory")
    pd_subcatid = models.ForeignKey(Osubcatergory, on_delete=models.CASCADE, verbose_name="Sub Catergory")
    pd_obrandid = models.ForeignKey(Obrands, on_delete=models.CASCADE, verbose_name="Brand")
    pd_ocountry = models.ForeignKey(Ocountry, on_delete=models.CASCADE, verbose_name="Country")
    pd_description = models.CharField(max_length=250, verbose_name="Description")
    pd_image = models.CharField(max_length=200, verbose_name="Image")

    class Meta:
        verbose_name = "Product"

    def __str__(self):
        return self.pd_name


class Oshp_price(models.Model):
    oshop = models.ForeignKey(Oshop, on_delete=models.CASCADE, verbose_name="Shop")
    oproduct = models.ForeignKey(Oproducts, on_delete=models.CASCADE, verbose_name="Product")
    oshop_price = models.PositiveIntegerField(default=0, verbose_name="Price")
    oprice_update_user = models.CharField(max_length=100)
    oprice_update_date = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "Shop Price"

    def __str__(self):
        return self.oshop_name


class opackingsize(models.Model):
    oproduct = models.ForeignKey(Oproducts, on_delete=models.CASCADE)
    ozpacking = models.ForeignKey(Opacking, on_delete=models.CASCADE)
    ozpacking_size = models.PositiveIntegerField(default=0)
    ozpacking_unit = models.PositiveIntegerField(default=0)
    ozproduct_code = models.CharField(max_length=100)
    oz_update_user = models.CharField(max_length=100)
    oz_update_date = models.DateTimeField(default=datetime.now)
