import requests

from check_url.models import Url


# Проверяем status_code url и записываем результат
def check_url(site_url):
    url = Url.objects.get(url=site_url)
    req = requests.get(url.url)
    if req.status_code == 200:
        url.status = True
    else:
        url.status = False
    url.save()
    return f'status: {req.status_code}'
