# Generated by Django 2.1.3 on 2019-09-12 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inoks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='tc',
            field=models.CharField(max_length=11, verbose_name='T.C. Kimlik Numarası'),
        ),
    ]