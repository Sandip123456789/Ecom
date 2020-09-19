# Generated by Django 3.1.1 on 2020-09-07 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='phone1',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='phone2',
            field=models.IntegerField(null=True),
        ),
    ]
