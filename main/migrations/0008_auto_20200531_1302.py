# Generated by Django 3.0.6 on 2020-05-31 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200531_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileimage',
            name='profile_image',
            field=models.ImageField(default='avatar.png', upload_to='profile'),
        ),
    ]
