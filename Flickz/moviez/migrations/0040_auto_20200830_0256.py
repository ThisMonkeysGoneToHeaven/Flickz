# Generated by Django 3.1 on 2020-08-29 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviez', '0039_auto_20200830_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='booking_time',
            field=models.IntegerField(default=1598736404, editable=False),
        ),
    ]