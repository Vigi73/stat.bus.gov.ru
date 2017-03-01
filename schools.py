from datetime import datetime
from libs import pars2
from inn_org import inns_school
from organization import get_value
from print_ import get_print_school, print_main_school, print_end_school

matrix = []
s_ = []


def get_schools():

    print_main_school()



    for i, inn in enumerate(inns_school, start=1):
        value1, value2, name_org = get_value(inn)

        urls = [f'http://bus.gov.ru/public/agency/agency_tasks.json?agency={value1}&d-5460-o=2&d-5460-s=1&task={value2}',
                f'http://bus.gov.ru/public/agency/last-budget.json?agency={value1}&d-5460-o=2&d-5460-s=1',
                f'http://bus.gov.ru/public/agency/last-annual-balance-F0503121-info.json?agencyId={value1}&d-5460-o=2&d-5460-s=1',
                f'http://bus.gov.ru/public/annual-balance-f0503127/show-last-annual-balance.json?agencyId={value1}&d-5460-o=2&d-5460-s=1',
                f'http://bus.gov.ru/public/agency/last_agency_balances_f0503130.json?agencyId={value1}&d-5460-o=2&d-5460-s=1',
                f'http://bus.gov.ru/public/agency/last_activity_estate_usage_report.json?agency={value1}&d-5460-o=2&d-5460-s=1',
                f'http://bus.gov.ru/public/agency/last-measure-details.json?agency={value1}&d-5460-o=2&d-5460-s=1'
                ]

        result = pars2(urls, inn)


        buh = sum([result[2], result[3], result[4]])
        if buh == 3:
            s_.append(1)

        pr = sum(result) * 100 / 7

        get_print_school(i, name_org, result, pr, "+" if pr == 100.0 else "")
        matrix.append(result)



    p1 = sum([matrix[j][0] for j in range(len(matrix))])
    p2 = sum([matrix[j][1] for j in range(len(matrix))])
    p3 = sum(s_)
    p6 = sum([matrix[j][5] for j in range(len(matrix))])
    p7 = sum([matrix[j][6] for j in range(len(matrix))])

    print_end_school(p1, p2, p3, p6, p7)