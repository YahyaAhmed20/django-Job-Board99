# Generated by Django 4.1 on 2022-10-23 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]