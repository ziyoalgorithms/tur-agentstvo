# Generated by Django 4.0.4 on 2022-05-28 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traveluserprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Man'), ('W', 'Woman')], max_length=1, verbose_name='gender'),
        ),
    ]