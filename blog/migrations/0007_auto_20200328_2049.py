# Generated by Django 3.0.4 on 2020-03-28 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200328_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='subject',
            field=models.CharField(choices=[('Anglický jazyk', 'Anglický jazyk'), ('Biologie', 'Biologie'), ('Český jazyk a literatura', 'Český jazyk a literatura'), ('Jazyky', 'Jazyky'), ('Fyzika', 'Fyzika'), ('Chemie', 'Chemie'), ('Matematika', 'Matematika'), ('Společenské vědy', 'Společenské vědy'), ('Zeměpis', 'Zeměpis'), ('Volitelné předměty', 'Volitelné předměty'), ('Ostatní', 'Ostatní')], default=('Ostatní', 'Ostatní'), max_length=100),
        ),
    ]