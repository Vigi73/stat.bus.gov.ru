from datetime import datetime


def get_print(i, org, lst, pr, buh):

    with open('otchet.txt', 'a', encoding='utf-8') as f:
        print('-' * 127, file=f)
        print(f'|{i:^{5}}|{org:<{65}}|{lst[0]:^{5}}|{lst[1]:^{5}}|{lst[2]:^{5}}|{lst[3]:^{5}}|{lst[4]:^{5}}|'
              f'{lst[5]:^{5}}|{lst[6]:^{5}}|{lst[7]:^{5}}|{pr:^{5}.{4}}|  {buh}', file=f)

def get_print_school(i, org, lst, pr, buh):
    with open('otchet.txt', 'a', encoding='utf-8') as f:
        print('-' * 121, file=f)
        print(f'|{i:^{5}}|{org:<{65}}|{lst[0]:^{5}}|{lst[1]:^{5}}|{lst[2]:^{5}}|{lst[3]:^{5}}|{lst[4]:^{5}}|'
              f'{lst[5]:^{5}}|{lst[6]:^{5}}|{pr:^{5}.{4}}|  {buh}', file=f)




def print_main():
    with open('otchet.txt', 'a', encoding='utf-8') as f:
        print(str(datetime.today().now()).split('.')[0], file=f)
        print('-' * 127, file=f)
        print(f'|{"№":^{5}}|{"ОРГАНИЗАЦИЯ":^{65}}|{"ГМЗ":^{5}}|{"ПФХД":^{5}}|{"ЦСБ":^{5}}|{"OФР":^{5}}|'
              f'{"БГУ":^{5}}|{"ИУП":^{5}}|{"ИРД":^{5}}|{"СКМ":^{5}}|{"%":^{5}}|', file=f)



def print_main_school():
    with open('otchet.txt', 'a', encoding='utf-8') as f:
        print('-' * 121, file=f)
        print(f'|{"№":^{5}}|{"ОРГАНИЗАЦИЯ":^{65}}|{"ГМЗ":^{5}}|{"БС":^{5}}|{"ОФР":^{5}}|{"ОИБ":^{5}}|'
              f'{"БЛС":^{5}}|{"ИРД":^{5}}|{"СКМ":^{5}}|{"%":^{5}}|', file=f)




def print_end(p1, p2, p3, p5,  p7, p8):
    with open('otchet.txt', 'a', encoding='utf-8') as f:
        print('-' * 127, file=f)
        print(f'|{" ":^{5}}|{"Итог":^{65}}|{p1:^{5}}|{p2:^{5}}|{p3:^{5}}|{" ":^{5}}|'
              f'{p5:^{5}}|{" ":^{5}}|{p7:^{5}}|{p8:^{5}}|{" ":^{5}}|', file=f)
        print('-' * 127, file=f)
        print(file=f)


def print_end_school(p1, p2, p3, p6,  p7):
    with open('otchet.txt', 'a', encoding='utf-8') as f:
        print('-' * 121, file=f)
        print(f'|{" ":^{5}}|{"Итог":^{65}}|{p1:^{5}}|{p2:^{5}}|{" ":^{5}}|{p3:^{5}}|'
              f'{" ":^{5}}|{p6:^{5}}|{p7:^{5}}|{" ":^{5}}|', file=f)
        print('-' * 121, file=f)
        print(file=f)



