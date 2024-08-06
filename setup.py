from setuptools import setup, find_packages

setup(
    name='my_aws_cli_tool',
    version='0.1',
    py_modules=['main'],
    install_requires=[
        'click',
        'boto3',
    ],
    entry_points='''
        [console_scripts]
        my_aws_cli_tool=main:cli
    ''',
)
