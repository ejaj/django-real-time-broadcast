# Generated by Django 4.1.7 on 2023-03-20 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MandrillEvents",
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
                (
                    "message_id",
                    models.CharField(
                        blank=True, max_length=250, null=True, verbose_name="Message ID"
                    ),
                ),
                (
                    "event_name",
                    models.CharField(
                        blank=True, max_length=250, null=True, verbose_name="Event Name"
                    ),
                ),
                (
                    "subject",
                    models.CharField(
                        blank=True, max_length=250, null=True, verbose_name="Subject"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, null=True, verbose_name="Email"
                    ),
                ),
                (
                    "sender",
                    models.EmailField(
                        blank=True, max_length=254, null=True, verbose_name="Sender"
                    ),
                ),
                ("tags", models.JSONField(blank=True, null=True, verbose_name="Tags")),
                (
                    "state",
                    models.CharField(
                        blank=True, max_length=250, null=True, verbose_name="State"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "mandrill_events",
                "ordering": ["-updated_at"],
            },
        ),
    ]