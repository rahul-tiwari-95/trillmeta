# Generated by Django 4.0.5 on 2022-10-25 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='category_name',
            field=models.TextField(choices=[('SHIRTS', 'SHIRTS'), ('BOTTOMS', 'BOTTOMS'), ('SNEAKERS', 'SNEAKERS'), ('THERMALS', 'THERMALS'), ('SHORTS', 'SHORTS'), ('HOME-DECOR', 'HOME-DECOR'), ('DIGITAL-ART', 'DIGITAL-ART'), ('MUSIC-FILE', 'MUSIC-FILE'), ('COLLECTIBLES', 'COLLECTIBLES'), ('DIGITAL-COLLECTIBLES', 'DIGITAL-COLLECTIBLES'), ('PHYSICAL-ACCESSORIES', 'PHYSICAL-ACCESSORIES'), ('ENTERTAINMENT', 'ENTERTAINMENT'), ('CREATORS', 'CREATORS'), ('INFLUENCERS', 'INFLUENCERS'), ('PHYSCIAL-PRODUCTS', 'PHYSCIAL-PRODUCTS')]),
        ),
    ]
