# Generated by Django 4.2.7 on 2023-12-31 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_bookmodel_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodel',
            name='quantity',
            field=models.IntegerField(blank=True, default=20, null=True),
        ),
    ]
