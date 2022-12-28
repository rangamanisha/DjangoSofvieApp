# Generated by Django 4.0 on 2022-12-28 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_citymodel_emplyeemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=120)),
                ('dob', models.DateTimeField()),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.statemodel')),
            ],
        ),
        migrations.DeleteModel(
            name='EmplyeeModel',
        ),
    ]
