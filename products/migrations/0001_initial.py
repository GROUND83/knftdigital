# Generated by Django 3.2 on 2022-03-13 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('files', '0001_initial'),
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='작품 타이틀')),
                ('description', models.TextField(blank=True, null=True, verbose_name='작품 설명')),
                ('creationDate', models.DateField(blank=True, null=True)),
                ('type', models.CharField(blank=True, choices=[('Notable', 'Notable'), ('Caligraphy', 'Caligraphy'), ('Engraving', 'Engraving'), ('Illustration', 'Illustration'), ('Photography', 'Photography')], default='Caligraphy', max_length=40, null=True, verbose_name='type')),
                ('dimensionsx', models.CharField(blank=True, max_length=10, null=True, verbose_name='x 사이즈')),
                ('dimensionsy', models.CharField(blank=True, max_length=10, null=True, verbose_name='y 사이즈')),
                ('projectType', models.CharField(blank=True, choices=[('the Love', 'the Love'), ('the Load', 'the Load')], default='the Love', max_length=40, null=True, verbose_name='project type')),
                ('productType', models.CharField(blank=True, choices=[('project', 'project'), ('edition', 'edition'), ('other', 'other')], default='project', max_length=40, null=True, verbose_name='product type')),
                ('projectTitle', models.CharField(blank=True, max_length=100, null=True, verbose_name='project title')),
                ('edtionTitle', models.CharField(blank=True, max_length=100, null=True, verbose_name='edtion title')),
                ('otherTitle', models.CharField(blank=True, max_length=100, null=True, verbose_name='other title')),
                ('foundataionLink', models.CharField(blank=True, max_length=50, null=True, verbose_name='foundataionLink')),
                ('openseaLink', models.CharField(blank=True, max_length=50, null=True, verbose_name='openseaLink')),
                ('solahartLink', models.CharField(blank=True, max_length=50, null=True, verbose_name='solahartLink')),
                ('raribleLink', models.CharField(blank=True, max_length=50, null=True, verbose_name='raribleLink')),
                ('main', models.BooleanField(default=False, verbose_name='메인작품')),
                ('number', models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='작품넘버')),
                ('hit', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='hit')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='ETH 가격')),
                ('theme', models.CharField(max_length=100, null=True, verbose_name='theme')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='authors.author')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='files.file')),
                ('tags', models.ManyToManyField(blank=True, null=True, to='products.Tag', verbose_name='tag')),
            ],
            options={
                'verbose_name': '작품',
                'verbose_name_plural': '작품',
                'ordering': ['title'],
            },
        ),
    ]
