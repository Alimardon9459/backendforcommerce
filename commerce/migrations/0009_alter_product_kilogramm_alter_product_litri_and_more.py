# Generated by Django 4.0.3 on 2022-06-29 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0008_rename_categoriya_product_mahsulot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='kilogramm',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='litri',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='narx',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='soni',
            field=models.IntegerField(null=True),
        ),
    ]