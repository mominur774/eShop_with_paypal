# Generated by Django 4.0.1 on 2022-02-02 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Processing', 'Processing'), ('On the Way', 'On the Way'), ('Completed', 'Completed')], default='Pending', max_length=50),
        ),
    ]
