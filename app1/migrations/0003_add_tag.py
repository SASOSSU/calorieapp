# Generated by Django 4.1 on 2022-08-07 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_category_alter_customer_options_customer_created_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=30)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.foods')),
            ],
        ),
    ]