import requests
from datetime import datetime

Y = '2017'


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
        r = requests.get(u, allow_redirects=False)
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
