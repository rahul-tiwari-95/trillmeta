# Generated by Django 4.0.5 on 2022-09-29 15:52

import backend.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_memories_bodegasubscriberledger_bodegapublicurl_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BodegaAnnouncementBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media1', models.FileField(default='8954256a-cc48-4d73-a863-5c8ebe3c426c.jpeg', upload_to='BodegaAnnouncementBanner/media1')),
                ('media2', models.FileField(default='8954256a-cc48-4d73-a863-5c8ebe3c426c.jpeg', upload_to='BodegaAnnouncementBanner/media2')),
                ('media3', models.FileField(default='8954256a-cc48-4d73-a863-5c8ebe3c426c.jpeg', upload_to='BodegaAnnouncementBanner/media3')),
                ('media4', models.FileField(default='8954256a-cc48-4d73-a863-5c8ebe3c426c.jpeg', upload_to='BodegaAnnouncementBanner/media4')),
                ('media5', models.FileField(default='8954256a-cc48-4d73-a863-5c8ebe3c426c.jpeg', upload_to='BodegaAnnouncementBanner/media5')),
                ('media6', models.FileField(default='8954256a-cc48-4d73-a863-5c8ebe3c426c.jpeg', upload_to='BodegaAnnouncementBanner/media6')),
                ('media7', models.FileField(default='8954256a-cc48-4d73-a863-5c8ebe3c426c.jpeg', upload_to='BodegaAnnouncementBanner/media7')),
                ('media8', models.FileField(default='8954256a-cc48-4d73-a863-5c8ebe3c426c.jpeg', upload_to='BodegaAnnouncementBanner/media8')),
                ('media9', models.FileField(default='8954256a-cc48-4d73-a863-5c8ebe3c426c.jpeg', upload_to='BodegaAnnouncementBanner/media9')),
                ('media10', models.FileField(default='8954256a-cc48-4d73-a863-5c8ebe3c426c.jpeg', upload_to='BodegaAnnouncementBanner/media10')),
                ('swiftURL1', models.TextField(blank=True)),
                ('swiftURL2', models.TextField(blank=True)),
                ('swiftURL3', models.TextField(blank=True)),
                ('swiftURL4', models.TextField(blank=True)),
                ('swiftURL5', models.TextField(blank=True)),
                ('swiftURL6', models.TextField(blank=True)),
                ('swiftURL7', models.TextField(blank=True)),
                ('swiftURL8', models.TextField(blank=True)),
                ('swiftURL9', models.TextField(blank=True)),
                ('swiftURL10', models.TextField(blank=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='productinventory',
            name='productID',
        ),
        migrations.AddField(
            model_name='bodegapublicurl',
            name='altText1',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='bodegapublicurl',
            name='altText10',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='bodegapublicurl',
            name='altText11',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='bodegapublicurl',
            name='altText12',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='bodegapublicurl',
            name='altText13',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='bodegapublicurl',
            name='altText14',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='bodegapublicurl',
            name='altText15',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='bodegapublicurl',
            name='altText2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='bodegapublicurl',
            name='altText3',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='bodegapublicurl',
            name='altText4',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='bodegapublicurl',
            name='altText5',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='bodegapublicurl',
            name='altText6',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='bodegapublicurl',
            name='altText7',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='bodegapublicurl',
            name='altText8',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='bodegapublicurl',
            name='altText9',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='message',
            name='messageMedia',
            field=models.FileField(default='8954256a-cc48-4d73-a863-5c8ebe3c426c.jpeg', upload_to='bodegaMessaging/message/'),
        ),
        migrations.AddField(
            model_name='metauseraccountstatus',
            name='creatorSubscriber',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='metauseraccountstatus',
            name='influencerSubscriber',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='metauseraccountstatus',
            name='rookieSubscriber',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='productInventoryID',
            field=models.ForeignKey(default=backend.models.get_sentinel_productInventory_id, on_delete=models.SET(backend.models.get_sentinel_productInventory), to='backend.productinventory'),
        ),
        migrations.AlterField(
            model_name='bodegapublicurl',
            name='media10',
            field=models.FileField(default='8954256a-cc48-4d73-a863-5c8ebe3c426c.jpeg', upload_to='bodegaMerchant/bodegaPublicURL/contentPage/media10'),
        ),
        migrations.AlterField(
            model_name='bodegapublicurl',
            name='media11',
            field=models.FileField(default='8954256a-cc48-4d73-a863-5c8ebe3c426c.jpeg', upload_to='bodegaMerchant/bodegaPublicURL/contentPage/media11'),
        ),
        migrations.AlterField(
            model_name='bodegapublicurl',
            name='media12',
            field=models.FileField(default='8954256a-cc48-4d73-a863-5c8ebe3c426c.jpeg', upload_to='bodegaMerchant/bodegaPublicURL/contentPage/media12'),
        ),
        migrations.AlterField(
            model_name='bodegapublicurl',
            name='media13',
            field=models.FileField(default='8954256a-cc48-4d73-a863-5c8ebe3c426c.jpeg', upload_to='bodegaMerchant/bodegaPublicURL/contentPage/media13'),
        ),
        migrations.AlterField(
            model_name='bodegapublicurl',
            name='media14',
            field=models.FileField(default='8954256a-cc48-4d73-a863-5c8ebe3c426c.jpeg', upload_to='bodegaMerchant/bodegaPublicURL/contentPage/media14'),
        ),
        migrations.AlterField(
            model_name='bodegapublicurl',
            name='media15',
            field=models.FileField(default='8954256a-cc48-4d73-a863-5c8ebe3c426c.jpeg', upload_to='bodegaMerchant/bodegaPublicURL/contentPage/media15'),
        ),
        migrations.AlterField(
            model_name='bodegapublicurl',
            name='media7',
            field=models.FileField(default='8954256a-cc48-4d73-a863-5c8ebe3c426c.jpeg', upload_to='bodegaMerchant/bodegaPublicURL/contentPage/media7'),
        ),
        migrations.AlterField(
            model_name='bodegapublicurl',
            name='media8',
            field=models.FileField(default='8954256a-cc48-4d73-a863-5c8ebe3c426c.jpeg', upload_to='bodegaMerchant/bodegaPublicURL/contentPage/media8'),
        ),
        migrations.AlterField(
            model_name='bodegapublicurl',
            name='media9',
            field=models.FileField(default='8954256a-cc48-4d73-a863-5c8ebe3c426c.jpeg', upload_to='bodegaMerchant/bodegaPublicURL/contentPage/media9'),
        ),
        migrations.AlterField(
            model_name='boosttags',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.metauser'),
        ),
        migrations.AlterField(
            model_name='boosttags',
            name='tags',
            field=models.CharField(max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='level',
            name='number',
            field=models.FloatField(default=5.0),
        ),
        migrations.AlterField(
            model_name='metauser',
            name='discord_username',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='metausertags',
            name='metauserStatus',
            field=models.CharField(default='ACTIVE CREATOR BODEGA1k', max_length=255),
        ),
    ]