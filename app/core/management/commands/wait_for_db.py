from django.core.management.base import BaseCommand
import time
from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Database Available!'))
        db_up = False

        while not db_up:
            try:
                self.check(databases=['default'])
                db_up = True
                time.sleep(2)
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second')
                time.sleep(1)

        self.stderr.write(self.style.SUCCESS('Database Available!'))
