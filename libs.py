import requests
from datetime import datetime
from fake_useragent import UserAgent

ua = UserAgent()
Y = '2017'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0',
           'Host': 'bus.gov.ru',
           'Accept': 'application/json, text/plain, */*',
           'Cookie': 'srv=29120; srv=29120; JSESSIONID=0000Cxo3aeWqAsuuUscGt0gCkgL:1846164jo; stick=!P5StB4HH86il6xkW1/kkDaZKycN1KVcbuZVArEfdX1L+/MiJOmx6/f57UngZtB/qKNFUToQttfZ3XWw=; srv=29120; gmuportal=3; _ym_uid=1488334556832746636; _ym_isad=2; _ym_visorc_14477227=w; gmuind=0; JSESSIONID=0000xFkAXe4ArTMp9-jr5wLMQHb:19t8nac8v; homeRegionId=5277388; homeRegionName=%D0%90%D0%BB%D1%82%D0%B0%D0%B9%D1%81%D0%BA%D0%B8%D0%B9; homeRegionFullName=%D0%90%D0%BB%D1%82%D0%B0%D0%B9%D1%81%D0%BA%D0%B8%D0%B9%20%D0%BA%D1%80%D0%B0%D0%B9; areaId=0; ppoId=1'}





def get_size(size, inn):
    or_p = {'2254002252': size-4,
            '2254003175': size-4,
            '2254003224': size-4,
            '2254002816': size-4,
            '2254003136': size-4,
            '2254002622': size-4,
            '2254003658': size-4,
            '2254002654': size-4,
            '2254002848': size-4,
            '2254002661': size-4,
            '2254003489': size-1,
            '2254002862': size-4,
            '2254003506': size-4,
            '2254003810': size-4,
            '2254003295': size-2
            }
    return or_p[inn]


def get_output(data):
    return datetime.fromtimestamp(data / 1000.0).strftime('%Y-%m-%d %H:%M:%S').split('-')[0]


def pars(urls, inn):
    list_answer = []

    for inc, u in enumerate(urls):

        r = requests.get(u,  headers=headers)
        data = r.json()


        try:
            list_answer.append(1 if get_output(data['currentTask']['publishDate']) == Y else 0)
        except KeyError:
            try:
                if inc == 1:
                    list_answer.append(1 if get_output(data['current']['publishDate']) == Y else 0)
                else:
                    list_answer.append(get_size(len(data['reports']), inn))
            except KeyError:
                try:
                    list_answer.append(1 if get_output(data['currentOperation']['publishDate']) == Y else 0)
                except KeyError:
                    try:
                        list_answer.append(1 if get_output(data['annualBalance']['publishDate']) == Y else 0)
                    except KeyError:
                        try:
                            list_answer.append(1 if get_output(data['balance']['publishDate']) == Y else 0)
                        except KeyError:
                            list_answer.append(1 if get_output(data['currentMeasureInfo']['publishDate']).
                                               split('-')[0] == Y else 0)
    return list_answer
