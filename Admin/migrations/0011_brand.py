# Generated by Django 4.1.5 on 2023-10-21 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0010_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
