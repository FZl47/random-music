import logging
import random
import string

from django.utils import timezone

_logger = logging.getLogger()


def random_str(n=7, characters=string.ascii_letters + string.digits):
    return ''.join(random.choice(characters) for _ in range(n))


def get_time(frmt='%Y-%m-%d'):
    return timezone.now().strftime(frmt)


def log_event(msg, level='info', exc_info=False, **kwargs):
    level = level.upper()
    levels = {
        'NOTSET': 0,
        'DEBUG': 10,
        'INFO': 20,
        'WARNING': 30,
        'ERROR': 40,
        'CRITICAL': 50,
    }
    logging.log(levels[level], msg=msg, exc_info=exc_info, **kwargs)
