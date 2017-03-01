import requests
from datetime import datetime
from fake_useragent import UserAgent
from time import sleep

ua = UserAgent()
Y = '2017'
headers = {'User-Agent': f'{ua.ie}'}


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
            '2254003295': size-2,
            '2254002693': size-4,
            '2254002647': size-4,
            '2254002598': size-4,
            '2254002630': size-4,
            '2254002679': size-4,
            '2254002580': size-4,
            '2254002573': size-4,
            '2254002686': size-4
            }
    return or_p[inn]


def get_output(data):
    return datetime.fromtimestamp(data / 1000.0).strftime('%Y-%m-%d %H:%M:%S').split('-')[0]


def pars(urls, inn):
    list_answer = []

    for inc, u in enumerate(urls):

        r = requests.get(u,  headers=headers, allow_redirects=False)#, proxies={'http': '138.68.141.222:8080'})
        print(r.status_code)
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
#============================================================================================

def pars2(urls, inn):
    list_answer = []

    for inc, u in enumerate(urls):

        r = requests.get(u,  headers=headers)#, allow_redirects=False)#, proxies={'http': '138.68.141.222:8080'})
        print(r.status_code)
        data = r.json()


        try:
            list_answer.append(1 if get_output(data['currentTask']['publishDate']) == Y else 0)
        except KeyError:
            try:
                list_answer.append(1 if get_output(data['currentBudget']['publishDate']) == Y else 0)
            except KeyError:
                try:
                    list_answer.append(1 if get_output(data['annualBalance']['publishDate']) == Y else 0)
                except:
                    try:
                        list_answer.append(1 if get_output(data['currentOperation']['publishDate']) == Y else 0)
                    except:
                        try:
                            list_answer.append(1 if get_output(data['currentOperation']['publishDate']) == Y else 0)
                        except:
                            try:
                                list_answer.append(get_size(len(data['reports']), inn))
                            except:
                                try:
                                    list_answer.append(1 if get_output(data['currentMeasureInfo']['publishDate']) ==
                                                            Y else 0)
                                except:
                                    list_answer.append('-')



    return list_answer



