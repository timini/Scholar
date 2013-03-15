from distutils.core import setup

setup(
    name='Scholarp',
    version='0.1.0',
    author='Christian Kreibich',
    py_modules=['scholar.py'],
    url='http://www.icir.org/christian/scholar.html',
    description='Python script for accessing Google Scholar, since it doesn\'t have an api.',
    long_description=open('README.md').read(),
)
