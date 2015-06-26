try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Python connector to mundipagg smartwallet api',
    'author': 'Mateus Zitelli <zitellimateu@gmail.com>',
    # 'url': 'URL to get it at.',
    # 'download_url': 'Where to download it.',
    'author_email': 'zitellimateus@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['MundipaggSmartwallet'],
    'scripts': [],
    'name': 'MundipaggSmartwallet'
}

setup(**config)
