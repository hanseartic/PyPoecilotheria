from setuptools import setup

setup(
    name='pypoeci',
    version='0.1.0',
    description='Python Poecilotheria - a nested spider',
    url='http://github.com/hanseartic/pypoeci',
    author='Paul Schuette',
    author_email='paul@hanseartic.de',
    license='MIT',
    packages=['pypoeci'],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
    ],
    install_requires=[
        'cssselect',
        'lxml',
        'PyDispatcher',
        'requests',
        'db-sqlite3',
    ],
    zip_safe=True,
)
