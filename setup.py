import setuptools

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





)
