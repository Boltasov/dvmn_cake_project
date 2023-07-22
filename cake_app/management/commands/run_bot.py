from django.core.management.base import BaseCommand
from tg_bot.cakebot import run_bot


class Command(BaseCommand):
    help = 'run bot'

    def handle(self, *args, **options):
        run_bot()
