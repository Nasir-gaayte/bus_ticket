# Generated by Django 4.1.2 on 2023-01-03 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketmodel',
            name='to',
            field=models.CharField(choices=[('bosaso to lascano', 'btl'), ('bosaso to garowe', 'btg'), ('bosaso to galkacyo', 'btgl'), ('bosaso to qardho', 'btq'), ('non', 'non')], default='non', max_length=255, verbose_name='toto'),
        ),
    ]
