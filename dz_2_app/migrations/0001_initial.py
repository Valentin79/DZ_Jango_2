# Generated by Django 4.2.3 on 2023-07-31 19:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('quantity', models.IntegerField(default=0)),
                ('added', models.DateField(default=datetime.datetime(2023, 7, 31, 22, 52, 47, 719350))),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('birthday', models.DateField(default=datetime.datetime(2023, 7, 31, 22, 52, 47, 719350))),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('creation_date', models.DateField(default=datetime.datetime(2023, 7, 31, 22, 52, 47, 719350))),
                ('goods_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dz_2_app.goods')),
                ('user_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dz_2_app.user')),
            ],
        ),
    ]
