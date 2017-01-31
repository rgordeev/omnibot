import omnibot
from setuptools import setup, find_packages


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('CHANGES.rst') as changes_file:
    changes = changes_file.read()

with open('CONTRIBUTING.rst') as contributing_file:
    contributing = contributing_file.read()


setup(
    name=omnibot.__title__,
    version=omnibot.__version__,
    author=omnibot.__author__,
    url="https://github.com/rgordeev/omnibot",
    description="Generate fake messages",
    long_description='\n\n'.join((
        readme,
        changes,
        contributing,
    )),
    license=omnibot.__license__,
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
    ], install_requires=['certifi', 'urllib3', 'requests']
)
