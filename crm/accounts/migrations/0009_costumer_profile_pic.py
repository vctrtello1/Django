# Generated by Django 3.0.4 on 2020-03-28 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_costumer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='costumer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile1.png', null=True, upload_to=''),
        ),
    ]