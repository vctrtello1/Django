# Generated by Django 3.0.3 on 2020-03-20 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200319_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
