# Generated by Django 3.2 on 2022-03-17 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='helpType',
            field=models.CharField(blank=True, choices=[('-', '-'), ('Buying NFTs', 'Buying NFTs'), ('Question about NFT art', 'Question about NFT art'), ('Participating in an NFT project', 'Participating in an NFT project'), ('Question about K-NFT', 'Question about K-NFT'), ('Partnering with K-NFT', 'Partnering with K-NFT'), ('Other', 'Other')], default='Buying NFTs', max_length=200, null=True, verbose_name='helpType'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='message'),
        ),
    ]
