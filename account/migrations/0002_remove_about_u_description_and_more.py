# Generated by Django 5.0.4 on 2024-05-16 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about_u',
            name='description',
        ),
        migrations.RemoveField(
            model_name='about_u',
            name='feature_image',
        ),
        migrations.AlterField(
            model_name='product',
            name='skuId',
            field=models.CharField(max_length=50),
        ),
    ]
