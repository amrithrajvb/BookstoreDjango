# Generated by Django 3.2.6 on 2021-09-02 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0002_book_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('ordered', 'ordered'), ('delivered', 'delivered'), ('in_transit', 'in_transit'), ('cancelled', 'cancelled')], default='ordered', max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('expected_deliverydate', models.DateField(null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owner.book')),
            ],
        ),
    ]