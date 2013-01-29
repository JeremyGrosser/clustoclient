from setuptools import setup

setup(name='clustoclient',
      version='0.2',
      py_modules=['clustohttp'],
      scripts=['clusto-template'],
      install_requires=['jinja2', 'IPy'])
