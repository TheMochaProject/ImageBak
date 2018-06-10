import setuptools
import atexit
import sys
import os
from setuptools.command.install import install
#boilerplate code from https://stackoverflow.com/questions/20288711/post-install-script-with-python-setuptools
class CustomInstall(install):
    def run(self):
        def _post_install():
            def find_module_path():
                print("DEBUG: sys.path is: " + str(sys.path))
                for p in sys.path[1:]:
                    if "ImageBak" in p:
                        return os.path.join(p, "src")
            install_path = find_module_path()
            print("Executing post-install scripts...\nReplacing the existing ImageBak script...")
            print("DEBUG: install_path is " + install_path)
            with open("/usr/local/bin/ImageBak", 'w') as imagebak_script:
                imagebak_script.write("#!/bin/sh\npython3 " + install_path + "/__main__.py")
        atexit.register(_post_install)
        install.run(self)

setuptools.setup(
    name="ImageBak",
    version="0.6",
    author = "Ramesh Balaji",
    description = "Easily back up files important to you.",
    packages=setuptools.find_packages(),
    url="https://github.com/TheMochaProject/ImageBak",
    zip_safe = False,
    include_package_data = True,
    entry_points={
        'gui_scripts':[
            'ImageBak=src.__main__:main'
        ]
    },
    cmdclass={'install': CustomInstall}





)
