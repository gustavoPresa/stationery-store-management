# Generated by Django 4.2.1 on 2023-06-04 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("provider", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sale",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "invoice_number",
                    models.CharField(
                        max_length=10, unique=True, verbose_name="Número da Nota Fiscal"
                    ),
                ),
                ("amount", models.IntegerField(verbose_name="Quantidade de Produtos")),
                ("created_at", models.DateTimeField(verbose_name="Data de Criação")),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="provider.client",
                    ),
                ),
                (
                    "products",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="provider.product",
                    ),
                ),
                (
                    "seller",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="provider.seller",
                    ),
                ),
            ],
        ),
    ]