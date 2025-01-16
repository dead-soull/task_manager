from setuptools import setup, find_packages

setup(
    name='dtaskcli',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'click'
    ],
    entry_points='''
    [console_scripts]
    dtask=dtaskcli:dtaskcli
    '''
)