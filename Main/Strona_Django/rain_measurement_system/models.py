# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    action_flag = models.PositiveSmallIntegerField()
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
    id = models.BigAutoField(primary_key=True)
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


class Logs(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    data_zdarzenia = models.DateField(db_column='Data_zdarzenia')  # Field name made lowercase.
    godzina_zdarzenia = models.TimeField(db_column='Godzina_zdarzenia')  # Field name made lowercase.
    opis_zdarzenia = models.CharField(db_column='Opis_zdarzenia', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'logs'


class RainGaugae(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    data_odczytu = models.DateField(db_column='Data_odczytu')  # Field name made lowercase.
    godzina_odczytu = models.TimeField(db_column='Godzina_odczytu')  # Field name made lowercase.
    wartosc = models.IntegerField(db_column='Wartosc')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rain_gaugae'


class RainSensor(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    data_odczytu = models.DateField(db_column='Data_odczytu')  # Field name made lowercase.
    godzina_odczytu = models.TimeField(db_column='Godzina_odczytu')  # Field name made lowercase.
    wartosc = models.IntegerField(db_column='Wartosc')  # Field name made lowercase.
    wartosc_tekstowa = models.CharField(db_column='Wartosc_tekstowa', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rain_sensor'


class WaterSensor(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    data_odczytu = models.DateField(db_column='Data_odczytu')  # Field name made lowercase.
    godzina_odczytu = models.TimeField(db_column='Godzina_odczytu')  # Field name made lowercase.
    wartosc = models.IntegerField(db_column='Wartosc')  # Field name made lowercase.
    wartosc_tekstowa = models.CharField(db_column='Wartosc_tekstowa', max_length=255)  # Field name made lowercase.
    alert = models.CharField(db_column='Alert', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'water_sensor'
