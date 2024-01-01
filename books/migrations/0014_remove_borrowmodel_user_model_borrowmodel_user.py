# Generated by Django 4.2.7 on 2023-12-31 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_remove_borrowmodel_user_borrowmodel_user_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrowmodel',
            name='user_model',
        ),
        migrations.AddField(
            model_name='borrowmodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.usermodel'),
        ),
    ]
