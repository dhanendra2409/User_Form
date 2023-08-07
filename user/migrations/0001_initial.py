# Generated by Django 4.2.3 on 2023-08-05 06:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserForm",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=500, null=True)),
                (
                    "photo",
                    models.FileField(blank=True, null=True, upload_to="uploads/photo/"),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, null=True, unique=True
                    ),
                ),
                (
                    "contact_no",
                    models.CharField(
                        blank=True,
                        error_messages={
                            "unique": "Mobile number is already registered"
                        },
                        max_length=10,
                        null=True,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="upto 10 digits", regex="^[6-9]\\d{9}$"
                            )
                        ],
                    ),
                ),
                (
                    "gurdian_mobile_no",
                    models.CharField(
                        blank=True,
                        max_length=10,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="upto 10 digits", regex="^[6-9]\\d{9}$"
                            )
                        ],
                    ),
                ),
                (
                    "id_proof",
                    models.FileField(
                        blank=True, null=True, upload_to="uploads/id_proof/"
                    ),
                ),
                (
                    "fathers_name",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                ("dob", models.DateField(blank=True, null=True)),
                (
                    "preparation_course",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                ("current_address", models.TextField(blank=True, null=True)),
                ("permanent_address", models.TextField(blank=True, null=True)),
                ("district", models.CharField(blank=True, max_length=500, null=True)),
                ("pincode", models.CharField(blank=True, max_length=6, null=True)),
                ("state", models.CharField(blank=True, max_length=500, null=True)),
                ("created_date", models.DateTimeField(auto_now_add=True, null=True)),
                ("modified_date", models.DateTimeField(auto_now=True, null=True)),
                ("timing_hrs", models.IntegerField(blank=True, null=True)),
                ("seat_no", models.IntegerField(blank=True, null=True)),
                ("session", models.IntegerField(blank=True, null=True)),
                ("want_copy", models.BooleanField(blank=True, null=True)),
                ("form_copy", models.FileField(blank=True, null=True, upload_to="")),
            ],
        ),
    ]