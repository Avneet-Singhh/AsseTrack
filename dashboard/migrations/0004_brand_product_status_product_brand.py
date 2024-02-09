# Generated by Django 4.2.5 on 2023-11-02 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Not-Available', 'Not-Available')], max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('Available', 'Available'), ('Not-Available', 'Not-Available')], default='Available', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='dashboard.brand'),
        ),
    ]
