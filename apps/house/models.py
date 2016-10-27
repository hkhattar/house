# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.db import models
import re
import bcrypt


from django.db import models

email_reg=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name_reg=re.compile(r'^[A-Za-z]{2,}$')
pin_reg=re.compile(r'^.{8,}$')
username_reg=re.compile(r'^[0-9a-zA-Z?-]{8,}$')

class UserManager(models.Manager):
    
    def register_valid(self,first,last,email,pin,confirm,username):
        error=[]
        if not name_reg.match(first):
            error.append("first name invalid")
        if not name_reg.match(last):
            error.append("last name invalid")
        if not email_reg.match(email):
            error.append("email invalid")
        if not pin_reg.match(pin):
            error.append("password too short")
        if pin!=confirm:
            error.append("confirm don't match with password")
        if not username_reg.match(username):
            error.append("username invalid")
        if User.objects.isExist(username):
            error.append("username is used, please choose a new one")
        return error

    def isExist(self,username):
        return User.objects.filter(username=username).exists()
    
    def login_valid(self,username,password):
        hashedpw=User.objects.get(username=username).password.encode()
        if bcrypt.hashpw(password.encode(),hashedpw)==hashedpw:
            return True
        else:
            return False

class User(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    username=models.CharField(max_length=30,null=True)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()


class PublicHousingAuthorities(models.Model):
    x = models.FloatField(db_column='X', blank=True, null=True)  # Field name made lowercase.
    y = models.FloatField(db_column='Y', blank=True, null=True)  # Field name made lowercase.
    formal_participant_name = models.TextField(db_column='FORMAL_PARTICIPANT_NAME', blank=True, null=True)  # Field name made lowercase.
    ha_phn_num = models.BigIntegerField(db_column='HA_PHN_NUM', blank=True, null=True)  # Field name made lowercase.
    ha_email_addr_text = models.TextField(db_column='HA_EMAIL_ADDR_TEXT', blank=True, null=True)  # Field name made lowercase.
    phas_designation = models.TextField(db_column='PHAS_DESIGNATION', blank=True, null=True)  # Field name made lowercase.
    ha_low_rent_size_category = models.TextField(db_column='HA_LOW_RENT_SIZE_CATEGORY', blank=True, null=True)  # Field name made lowercase.
    ha_program_type = models.TextField(db_column='HA_PROGRAM_TYPE', blank=True, null=True)  # Field name made lowercase.
    total_units = models.IntegerField(db_column='TOTAL_UNITS', blank=True, null=True)  # Field name made lowercase.
    total_occupied = models.IntegerField(db_column='TOTAL_OCCUPIED', blank=True, null=True)  # Field name made lowercase.
    pct_occupied = models.FloatField(db_column='PCT_OCCUPIED', blank=True, null=True)  # Field name made lowercase.
    pha_total_units = models.IntegerField(db_column='PHA_TOTAL_UNITS', blank=True, null=True)  # Field name made lowercase.
    spending_per_month = models.IntegerField(db_column='SPENDING_PER_MONTH', blank=True, null=True)  # Field name made lowercase.
    chldrn_mbr_cnt = models.IntegerField(db_column='CHLDRN_MBR_CNT', blank=True, null=True)  # Field name made lowercase.
    eldly_prcnt = models.FloatField(db_column='ELDLY_PRCNT', blank=True, null=True)  # Field name made lowercase.
    pct_disabled_lt62_all = models.FloatField(db_column='PCT_DISABLED_LT62_ALL', blank=True, null=True)  # Field name made lowercase.
    pct_lt80_median = models.FloatField(db_column='PCT_LT80_MEDIAN', blank=True, null=True)  # Field name made lowercase.
    median_inc_amnt = models.IntegerField(db_column='MEDIAN_INC_AMNT', blank=True, null=True)  # Field name made lowercase.
    curcnty_nm = models.TextField(db_column='CURCNTY_NM', blank=True, null=True)  # Field name made lowercase.
    std_addr = models.TextField(db_column='STD_ADDR', blank=True, null=True)  # Field name made lowercase.
    std_city = models.TextField(db_column='STD_CITY', blank=True, null=True)  # Field name made lowercase.
    std_st = models.TextField(db_column='STD_ST', blank=True, null=True)  # Field name made lowercase.
    std_zip5 = models.IntegerField(db_column='STD_ZIP5', blank=True, null=True)  # Field name made lowercase.
    lat = models.FloatField(db_column='LAT', blank=True, null=True)  # Field name made lowercase.
    lon = models.FloatField(db_column='LON', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Public_Housing_Authorities'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class HouseUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'house_user'
