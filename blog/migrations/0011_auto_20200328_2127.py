# Generated by Django 3.0.4 on 2020-03-28 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200328_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='subject',
            field=models.CharField(blank=True, choices=[('Anglický jazyk', 'AJ'), ('Biologie', 'Biologie'), ('Český jazyk a literatura', 'Český jazyk a literatura'), ('Jazyky', 'Jazyky'), ('Fyzika', 'Fyzika'), ('Chemie', 'Chemie'), ('Matematika', 'Matematika'), ('Společenské vědy', 'Společenské vědy'), ('Zeměpis', 'Zeměpis'), ('Volitelné předměty', 'Volitelné předměty'), ('Ostatní', 'Ostatní')], max_length=100, null=True),
        ),
    ]