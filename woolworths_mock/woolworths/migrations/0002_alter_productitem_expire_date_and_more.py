# Generated by Django 5.0.8 on 2024-08-13 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('woolworths', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productitem',
            name='expire_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='productitem',
            name='produce_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='discount',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='save_price',
            field=models.FloatField(default=0),
        ),
    ]
