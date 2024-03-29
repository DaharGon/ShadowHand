# Generated by Django 2.2 on 2019-08-19 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='', max_length=256)),
            ],
        ),
        migrations.AlterModelOptions(
            name='planet',
            options={'verbose_name': 'Планета', 'verbose_name_plural': 'Планеты'},
        ),
        migrations.AlterModelOptions(
            name='recruit',
            options={'verbose_name': 'Рекрут', 'verbose_name_plural': 'Рекруты'},
        ),
        migrations.AlterModelOptions(
            name='sith',
            options={'verbose_name': 'Ситх', 'verbose_name_plural': 'Ситхи'},
        ),
        migrations.AlterField(
            model_name='planet',
            name='name',
            field=models.CharField(default='', max_length=32, unique=True, verbose_name='Название планеты'),
        ),
        migrations.AlterField(
            model_name='recruit',
            name='planet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Planet', verbose_name='Планета'),
        ),
        migrations.AlterField(
            model_name='sith',
            name='name',
            field=models.CharField(default='', max_length=32, verbose_name='Имя ситха'),
        ),
        migrations.AlterField(
            model_name='sith',
            name='planet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Planet', verbose_name='Планета'),
        ),
    ]
