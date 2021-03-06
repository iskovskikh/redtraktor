# Generated by Django 2.0.4 on 2018-07-08 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20180708_0841'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='SpecUnits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='spec',
            name='caption',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='product.SpecItem'),
        ),
        migrations.DeleteModel(
            name='SpecList',
        ),
        migrations.AddField(
            model_name='specitem',
            name='unit',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.SpecUnits'),
        ),
    ]
