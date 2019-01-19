from distutils.core import setup

setup(
    name='Binarify',
    version='1.0.0',
    author='Rohit Midha',
    author_email='rohit.midha23@gmail.com',
    packages=['binarify'],
    license='LICENSE.txt',
    description='Convert any image to binary art.',
    long_description=open('README.txt').read(),
    install_requires=[
        "Pillow >= 3.4.0",
    ],
)
