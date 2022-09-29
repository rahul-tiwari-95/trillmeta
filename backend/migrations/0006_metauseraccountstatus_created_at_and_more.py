# Generated by Django 4.0.5 on 2022-09-06 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_subscribers_shopid_alter_bodegaserver_isroomprivate'),
    ]

    operations = [
        migrations.AddField(
            model_name='metauseraccountstatus',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='metauseraccountstatus',
            name='modified_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='metauseraccountstatus',
            name='referralCount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='metauseraccountstatus',
            name='referralStatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='metausertags',
            name='metauserStatus',
            field=models.CharField(default='ACTIVE CREATOR', max_length=255),
        ),
        migrations.AlterField(
            model_name='metausertags',
            name='trophiesAllocated',
            field=models.TextField(default='BODEGA100 REVOLUTIONARY'),
        ),
        migrations.CreateModel(
            name='BodegaServerParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bodegaServerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.bodegaserver')),
                ('metauserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.metauser')),
            ],
        ),
    ]