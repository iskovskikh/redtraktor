# Generated by Django 2.0.4 on 2018-07-08 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20180626_2056'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('val', models.CharField(max_length=256)),
            ],
        ),
        migrations.AlterField(
            model_name='spec',
            name='caption',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.SpecList'),
        ),
    ]