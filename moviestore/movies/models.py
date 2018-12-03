# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Locations(models.Model):
    streetone = models.CharField(db_column='streetOne', max_length=255, blank=True, null=True)  # Field name made lowercase.
    streettwo = models.CharField(db_column='streetTwo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(max_length=255, blank=True, null=True)
    postalcode = models.IntegerField(db_column='postalCode', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    stylistid = models.ForeignKey('Stylists', models.DO_NOTHING, db_column='stylistId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'locations'


class Photos(models.Model):
    photoname = models.CharField(db_column='photoName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    stylistid = models.ForeignKey('Stylists', models.DO_NOTHING, db_column='stylistId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'photos'


class Rates(models.Model):
    ratetype = models.CharField(db_column='rateType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    stylisttype = models.CharField(db_column='stylistType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ratevalue = models.FloatField(db_column='rateValue', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    stylistid = models.ForeignKey('Stylists', models.DO_NOTHING, db_column='stylistId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rates'


class Reviews(models.Model):
    review = models.TextField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    sessionid = models.ForeignKey('Sessions', models.DO_NOTHING, db_column='sessionId', blank=True, null=True)  # Field name made lowercase.
    salonid = models.ForeignKey('Salons', models.DO_NOTHING, db_column='salonId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reviews'


class Salons(models.Model):
    salonname = models.CharField(db_column='salonName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'salons'


class Sessions(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    sessiontype = models.CharField(db_column='sessionType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    stylistid = models.ForeignKey('Stylists', models.DO_NOTHING, db_column='stylistId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sessions'


class Skills(models.Model):
    skilltype = models.CharField(db_column='skillType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    stylistid = models.ForeignKey('Stylists', models.DO_NOTHING, db_column='stylistId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'skills'


class Stylists(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    qualification = models.CharField(max_length=255, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stylists'
