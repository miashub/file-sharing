# Generated by Django 5.2 on 2025-04-22 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fileapp", "0002_encryptedfile_file_size_encryptedfile_uploaded_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="encryptedfile",
            name="file_type",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
