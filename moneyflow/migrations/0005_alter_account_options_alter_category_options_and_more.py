# Generated by Django 4.2.6 on 2023-11-06 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('moneyflow', '0004_document_document_name_transaction_amount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'tili', 'verbose_name_plural': 'tilit'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'kategoria', 'verbose_name_plural': 'kategoriat'},
        ),
        migrations.AlterModelOptions(
            name='document',
            options={'verbose_name': 'dokumentti', 'verbose_name_plural': 'dokumentit'},
        ),
        migrations.AlterModelOptions(
            name='transaction',
            options={'verbose_name': 'tilitapahtuma', 'verbose_name_plural': 'tilitapahtumat'},
        ),
        migrations.AddField(
            model_name='transaction',
            name='transaction_comment',
            field=models.CharField(blank=True, max_length=200, verbose_name='kommentti'),
        ),
        migrations.AlterField(
            model_name='account',
            name='bank_account',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='pankkitili'),
        ),
        migrations.AlterField(
            model_name='account',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='aikaleima'),
        ),
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(max_length=200, verbose_name='nimi'),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='aikaleima'),
        ),
        migrations.AlterField(
            model_name='category',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='omistaja'),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='moneyflow.category'),
        ),
        migrations.AlterField(
            model_name='document',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='aikaleima'),
        ),
        migrations.AlterField(
            model_name='document',
            name='document_file',
            field=models.FileField(upload_to='docs/%Y-%m/', verbose_name='tiedosto'),
        ),
        migrations.AlterField(
            model_name='document',
            name='document_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='nimi'),
        ),
        migrations.AlterField(
            model_name='document',
            name='document_type',
            field=models.CharField(choices=[('BILL', 'Lasku'), ('RECEIPT', 'Kuitti'), ('CALCULATION', 'Laskelma'), ('OTHER', 'Muu')], max_length=20, verbose_name='tyyppi'),
        ),
        migrations.AlterField(
            model_name='document',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='omistaja'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='moneyflow.account', verbose_name='tili'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='maara'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='aikaleima'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='moneyflow.category', verbose_name='kategoria'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_date',
            field=models.DateField(verbose_name='paivays'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_documents',
            field=models.ManyToManyField(blank=True, related_name='transactions', to='moneyflow.document', verbose_name='dokumentit'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_state',
            field=models.CharField(choices=[('PENDING', 'Tuleva'), ('COMPLETE', 'Tapahtunut')], max_length=10, verbose_name='tila'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('IN', 'Tulo'), ('EXP', 'Meno')], max_length=10, verbose_name='tyyppi'),
        ),
    ]
