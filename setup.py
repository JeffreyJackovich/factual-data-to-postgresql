from setuptools import setup

setup(name='factual_data_to_postgresql',
      version='0.1',
      description='Extracts data from factual to Postgresql',
      url='https://github.com/JeffreyJackovich/factual_data_to_postgresql',
      author='Jeffrey Jackovich',
      license='MIT',
      packages=['factual_data_to_postgresql'],
     install_requires=['psycopg2==2.7.5',
                        'factual-api==1.7.0'])
