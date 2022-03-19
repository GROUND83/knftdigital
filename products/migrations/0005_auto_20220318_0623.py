# Generated by Django 3.2 on 2022-03-18 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20220318_0621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(blank=True, choices=[('Notable', 'Notable'), ('Caligraphy', 'Caligraphy'), ('Engraving', 'Engraving'), ('Illustration', 'Illustration'), ('Photography', 'Photography')], default='Caligraphy', max_length=40, null=True, verbose_name='type'),
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]
