# Generated by Django 4.1 on 2023-09-05 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flipkart', '0003_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
