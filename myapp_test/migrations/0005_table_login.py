# Generated by Django 4.1.1 on 2022-11-17 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp_test', '0004_rename_member_remark_table_members_member_surname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table_login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_login', models.CharField(max_length=30)),
                ('pass_login', models.CharField(max_length=30)),
                ('remark_login', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]