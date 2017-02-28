from datetime import datetime
from libs import pars
from inn_org import inns_mb
from organization import get_value
from print_ import get_print, print_main, print_end


if __name__ == '__main__':

    print_main()

    st_time = datetime.now()

    for i, inn in enumerate(inns_mb, start=1):
        value1, value2, name_org = get_value(inn)

        urls = [f'http://bus.gov.ru/public/agency/agency_tasks.json?agency={value1}&task={value2}',
                f'http://bus.gov.ru/public/agency/last-agency-plan.json?agency={value1}&d-5460-o=2&d-5460-s=1',
                f'http://bus.gov.ru/public/agency/last-operation.json?agency={value1}&stage=',
                f'http://bus.gov.ru/public/agency/last-annual-balance-F0503721-info.json?agencyId={value1}',
                f'http://bus.gov.ru/public/agency/last-annual-balance-F0503730-info.json?agencyId={value1}',
                f'http://bus.gov.ru/public/annual-balance-f0503737/show-last-annual-balance.json?agencyId={value1}',
                f'http://bus.gov.ru/public/agency/last_activity_estate_usage_report.json?agency={value1}',
                f'http://bus.gov.ru/public/agency/last-measure-details.json?agency={value1}'
                ]

        result = pars(urls, inn)
        pr = sum(result) * 100 / 8
        get_print(i, name_org, result, pr)

    print_end()
    end_time = datetime.now()

    print(str(end_time - st_time).split('.')[0])
