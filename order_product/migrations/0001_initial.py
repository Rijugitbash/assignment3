# Generated by Django 3.2.4 on 2023-11-09 07:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('location', models.CharField(default='None', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_at', models.DateTimeField(auto_now_add=True)),
                ('deliver_status', models.CharField(default='Pending', max_length=10)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_product.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
