from setuptools import setup

setup(name='monoprice_amplifier',
      version='0.0.1',
      description='Library to interface with Monoprice/Dayton multizone amplifiers through RS232',
      url='https://github.com/jetrich/monoprice_amplifier',
      download_url='https://github.com/jetrich/monoprice_amplifier/archive/0.0.1.tar.gz', #
      author='jetrich',
      license='MIT',
      packages=['monoprice_amplifier'],
      install_requires=['pyserial==3.2.1'],
      zip_safe=True) 
