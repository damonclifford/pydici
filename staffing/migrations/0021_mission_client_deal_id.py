# Generated by Django 3.2.19 on 2023-06-27 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staffing', '0020_alter_mission_min_charge_multiple_per_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='mission',
            name='client_deal_id',
            field=models.CharField(blank=True, max_length=100, verbose_name='Client deal id'),
        ),
    ]
