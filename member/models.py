from django.db import models

class AddressBook(models.Model):
    name            = models.CharField(max_length=45)
    firstname       = models.CharField(max_length=45)
    lastname        = models.CharField(max_length=45)
    company         = models.CharField(max_length=45)
    address1        = models.CharField(max_length=100)
    address2        = models.CharField(max_length=100)
    country         = models.CharField(max_length=45)
    zipcode         = models.CharField(max_length=10)
    city            = models.CharField(max_length=10)
    phone_number    = models.CharField(max_length=45)
    member          = models.ForeignKey('Member', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'address_books'

class Member(models.Model):
    firstname         = models.CharField(max_length=10)
    lastname          = models.CharField(max_length=10)
    email             = models.EmailField(max_length=50)
    social_login_type = models.ForeignKey('SocialLoginType', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'members'

class SocialLoginType(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'social_login_types'
