# Generated by Django 4.1.1 on 2022-09-27 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product_masters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pd_name', models.CharField(max_length=50, unique=True)),
                ('cat_name', models.CharField(default='', max_length=5)),
            ],
        ),
    ]
