# Generated migration to add amount_paid and balance fields to Order

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0022_payment_orderstatushistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount_paid',
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                help_text='Sum of all payments. Updated after each payment or refund.',
                max_digits=10,
            ),
        ),
        migrations.AddField(
            model_name='order',
            name='balance',
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                help_text='Remaining amount owed. Updated after each payment or refund.',
                max_digits=10,
            ),
        ),
    ]
