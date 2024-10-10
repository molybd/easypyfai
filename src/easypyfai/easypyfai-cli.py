import sys
from multiprocessing import Process

import silx
import pyFAI
import pyFAI.app
import pyFAI.app.calib2
import pyFAI.app.integrate
import silx.app
import silx.app.view
import silx.app.view.main


def app_silx_view():
    silx.app.view.main.main(sys.argv)
    
def app_pyfai_calib2():
    result = pyFAI.app.calib2.main()
    sys.exit(result)
    
def app_pyfai_integrate():
    pyFAI.app.integrate.main()


APPS = {
    'silx-view': app_silx_view,
    'pyFAI-calib2': app_pyfai_calib2,
    'pyFAI-integrate': app_pyfai_integrate,
}


def main():
    print('='*40)
    keys = list(APPS.keys())
    app_list_str = '\n'.join(f'[{i+1}] {key}' for i, key in enumerate(keys))
    print(app_list_str)
    index = input('Choose the index of APP to run: ')
    print('='*40)
    
    index = int(index)
    APPS[keys[index-1]]()
    

if __name__ == "__main__":
    main()
