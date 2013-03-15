from distutils.core import setup

setup(
    name='Scholar',
    version='0.0.1',
    author='Christian Kreibich',
    packages=['scholar',], 
    scripts=['scholar.py'],
    url='http://www.icir.org/christian/scholar.html',
    license='LICENSE.txt',
    description='Python script for accessing Google Scholar, since it doesn\'t have an api.',
    long_description=open('README.md').read(),
#    install_requires=[
#    ],
)
