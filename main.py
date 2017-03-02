from mb import get_mb
from schools import get_schools
from kray import get_kray
from avto import get_avto
from czn import get_czn
from datetime import datetime



if __name__ == '__main__':

    s = datetime.now()
    with open('otchet.txt', 'w') as f:
        print(file=f)


    get_mb()
    get_kray()
    get_avto()
    get_schools()
    get_czn()

    e = datetime.now()

    print(f'\nTime Using: {str(e-s)}')

