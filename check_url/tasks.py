from NII_Django.celery import app
from check_url.models import Url
from check_url.utils import check_url


# Запускаем несколько проверок url
@app.task()
def status_url():
    result_status = dict()
    list_urls = Url.objects.all()
    for url in list_urls:
        status = check_url(url.url)
        result_status[url.url] = status
    return result_status
