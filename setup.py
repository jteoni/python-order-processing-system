from setuptools import setup, find_packages

setup(
    name='order_processing_system',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pytest',
        'pydantic',
    ],
    entry_points={
        'console_scripts': [
            'process_orders=src.main:main',
        ],
    },
)
