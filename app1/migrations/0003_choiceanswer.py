# Generated by Django 3.0.4 on 2020-05-19 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20200518_0503'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChoiceAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Choice')),
            ],
        ),
    ]
