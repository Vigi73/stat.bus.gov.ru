from mb import get_mb
from schools import get_schools
from datetime import datetime

if __name__ == '__main__':

    s = datetime.now()

    get_mb()
    get_schools()

    e = datetime.now()

    print(f'\nTime Using: {str(e-s)}')