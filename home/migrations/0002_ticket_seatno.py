# Generated by Django 2.2.6 on 2019-11-02 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='seatno',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
