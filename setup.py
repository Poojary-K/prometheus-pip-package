from setuptools import setup, find_packages

setup(
    name='flask_prometheus_metrics',
    version='24.9.5',
    packages=['flask_prometheus_metrics'],
    install_requires=[
        'prometheus-client>=0.8.0'  # Specify the minimum version of prometheus-client
    ],
    py_modules=['flask_prometheus_metrics'],
    author='Poojary Karunakar',
    author_email='Poojary.K@mu-sigma.com',
    description='A package for integrating Prometheus metrics into Flask applications.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://gitlab.ird.mu-sigma.com/Poojary.K/prometheus-pip-package',  # Update with your repo URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Flask'
    ],
)
