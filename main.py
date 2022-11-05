import sys
import subprocess
import pkg_resources

def libraries_dependecies_check():
    """
    Check if needed libraries are installed. These are:
        - Numpy
        - Pandas
    """
    installed_packages = pkg_resources.working_set
    installed_packages_key = sorted([f'{i.key}' for i in installed_packages])
    libraries_pool = ['pandas', 'numpy', 'scipy', 'torch']

    for lib in libraries_pool:
        if lib in installed_packages_key:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', lib])
        else:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', lib])
            

libraries_dependecies_check()