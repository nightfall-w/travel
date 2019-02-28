import os
from celery import Celery
# ?celery??django????????
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "red_travel.settings")

# ??celery??
app = Celery('red_travel')

# ??celery??
app.config_from_object('django.conf:settings')

# ????celery??
app.autodiscover_tasks(['celery_tasks.SMS'])

