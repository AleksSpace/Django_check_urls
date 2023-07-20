import os

from celery import Celery

# Устанавливаем модуль настроек Django по умолчанию для «Celery».
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NII_Django.settings')

broker_url = os.environ.get('RABBITMQ_URL', 'amqp://guest:guest@localhost:5672/')

app = Celery('NII_Django', broker=broker_url)

# Запускаем задачу каждую минуту
app.conf.beat_schedule = {
    'add-every-60-seconds': {
        'task': 'check_url.tasks.status_url',
        'schedule': 60.0,
    },
}
app.conf.timezone = 'UTC'

# Использование здесь строки означает, что рабочему процессу не нужно сериализовать
# объект конфигурации дочерним процессам.
# - namespace='CELERY' означает все ключи конфигурации, связанные с сельдереем
# должен иметь префикс `CELERY_`.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Загружаем модули задач из всех зарегистрированных приложений Django.
app.autodiscover_tasks()
