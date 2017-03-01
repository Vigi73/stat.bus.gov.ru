
from libs import pars
from inn_org import inns_mb
from organization import get_value
from print_ import get_print, print_main, print_end
import progressbar


matrix = []
s_ = []

def get_mb():
    print_main()

    bar = progressbar.ProgressBar(maxval=150.0).start()
    t = 0.0

    for i, inn in enumerate(inns_mb, start=1):


        value1, value2, name_org = get_value(inn)

        urls = [f'http://bus.gov.ru/public/agency/agency_tasks.json?agency={value1}&d-5460-o=2&d-5460-s=1&task={value2}',
                f'http://bus.gov.ru/public/agency/last-agency-plan.json?agency={value1}&d-5460-o=2&d-5460-s=1',
                f'http://bus.gov.ru/public/agency/last-operation.json?agency={value1}&stage=',
                f'http://bus.gov.ru/public/agency/last-annual-balance-F0503721-info.json?agencyId={value1}&d-5460-o=2&d-5460-s=1',
                f'http://bus.gov.ru/public/agency/last-annual-balance-F0503730-info.json?agencyId={value1}',
                f'http://bus.gov.ru/public/annual-balance-f0503737/show-last-annual-balance.json?agencyId={value1}',
                f'http://bus.gov.ru/public/agency/last_activity_estate_usage_report.json?agency={value1}&d-5460-o=2&d-5460-s=1',
                f'http://bus.gov.ru/public/agency/last-measure-details.json?agency={value1}&d-5460-o=2&d-5460-s=1'
                ]

        result = pars(urls, inn)
        bar.update(t)
        t += 10.0

        buh = sum([result[3], result[4], result[5]])
        if buh == 3:
            s_.append(1)

        pr = sum(result) * 100 / 8
        get_print(i, name_org, result, pr, "+" if pr == 100.0 else "")
        matrix.append(result)

    bar.finish()
    p1 = sum([matrix[j][0] for j in range(len(matrix))])
    p2 = sum([matrix[j][1] for j in range(len(matrix))])
    p3 = sum([matrix[j][2] for j in range(len(matrix))])

    p5 = sum(s_)

    p7 = sum([matrix[j][6] for j in range(len(matrix))])
    p8 = sum([matrix[j][7] for j in range(len(matrix))])

    print_end(p1, p2, p3, p5, p7, p8)

