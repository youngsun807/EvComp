# Generated by Django 2.1.4 on 2019-01-02 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evComp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('publication_date1', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='analysis',
            name='author',
        ),
        migrations.RemoveField(
            model_name='analysis',
            name='publication_date1',
        ),
        migrations.AddField(
            model_name='analysis',
            name='beta',
            field=models.FloatField(default=1),
        ),
        migrations.AddField(
            model_name='analysis',
            name='ev',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='analysis',
            name='evps',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='analysis',
            name='re',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='analysis',
            name='rf',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='analysis',
            name='rm',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='code',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='report',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evComp.Company'),
        ),
    ]
