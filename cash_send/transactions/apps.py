import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TransactionsConfig(AppConfig):
    name = "transactions"
    verbose_name = _("Transactions")

    def ready(self):
        with contextlib.suppress(ImportError):
            import cash_send.transactions.signal
