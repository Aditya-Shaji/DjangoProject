# Generated by Django 4.2.5 on 2023-12-02 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0011_brand'),
        ('Guest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userregistration',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='userregistration',
            name='pincode',
        ),
        migrations.AddField(
            model_name='userregistration',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.district'),
        ),
        migrations.AddField(
            model_name='userregistration',
            name='file',
            field=models.FileField(null=True, upload_to='user/'),
        ),
    ]
