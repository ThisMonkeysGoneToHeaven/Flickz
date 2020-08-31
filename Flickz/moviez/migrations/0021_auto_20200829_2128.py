# Generated by Django 3.1 on 2020-08-29 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moviez', '0020_auto_20200829_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='booking_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='expired',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviez.movie'),
        ),
    ]