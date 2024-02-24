# Generated by Django 4.1.1 on 2024-02-24 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Varsity_Admin', '0001_initial'),
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SwapRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=200, null=True)),
                ('status', models.IntegerField(default=0, null=True)),
                ('hall', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Varsity_Admin.hall')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Student.student')),
            ],
        ),
        migrations.CreateModel(
            name='RepairRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=200, null=True)),
                ('status', models.IntegerField(default=0, null=True)),
                ('requestType', models.IntegerField(default=0, null=True)),
                ('hall', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Varsity_Admin.hall')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Student.student')),
            ],
        ),
    ]
