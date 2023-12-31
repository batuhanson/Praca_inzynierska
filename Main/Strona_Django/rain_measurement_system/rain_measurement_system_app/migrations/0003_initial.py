# Generated by Django 4.2.1 on 2023-09-17 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("rain_measurement_system_app", "0002_auto_20230915_1419"),
    ]

    operations = [
        migrations.CreateModel(
            name="Logs",
            fields=[
                (
                    "id",
                    models.AutoField(db_column="ID", primary_key=True, serialize=False),
                ),
                ("data_zdarzenia", models.DateField(db_column="Data_zdarzenia")),
                ("godzina_zdarzenia", models.TimeField(db_column="Godzina_zdarzenia")),
                (
                    "opis_zdarzenia",
                    models.CharField(db_column="Opis_zdarzenia", max_length=255),
                ),
            ],
            options={
                "db_table": "logs",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="RainGaugae",
            fields=[
                (
                    "id",
                    models.AutoField(db_column="ID", primary_key=True, serialize=False),
                ),
                ("data_odczytu", models.DateField(db_column="Data_odczytu")),
                ("godzina_odczytu", models.TimeField(db_column="Godzina_odczytu")),
                ("wartosc", models.IntegerField(db_column="Wartosc")),
            ],
            options={
                "db_table": "rain_gaugae",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="RainSensor",
            fields=[
                (
                    "id",
                    models.AutoField(db_column="ID", primary_key=True, serialize=False),
                ),
                ("data_odczytu", models.DateField(db_column="Data_odczytu")),
                ("godzina_odczytu", models.TimeField(db_column="Godzina_odczytu")),
                ("wartosc", models.IntegerField(db_column="Wartosc")),
                (
                    "wartosc_tekstowa",
                    models.CharField(db_column="Wartosc_tekstowa", max_length=255),
                ),
            ],
            options={
                "db_table": "rain_sensor",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="WaterSensor",
            fields=[
                (
                    "id",
                    models.AutoField(db_column="ID", primary_key=True, serialize=False),
                ),
                ("data_odczytu", models.DateField(db_column="Data_odczytu")),
                ("godzina_odczytu", models.TimeField(db_column="Godzina_odczytu")),
                ("wartosc", models.IntegerField(db_column="Wartosc")),
                (
                    "wartosc_tekstowa",
                    models.CharField(db_column="Wartosc_tekstowa", max_length=255),
                ),
                ("alert", models.CharField(db_column="Alert", max_length=255)),
            ],
            options={
                "db_table": "water_sensor",
                "managed": False,
            },
        ),
    ]
