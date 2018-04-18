# Packaging references:
# https://github.com/pypa/packaging/
# https://packaging.pypa.io/en/latest/
# https://setuptools.readthedocs.io/en/latest/setuptools.html

from setuptools import setup, find_packages

setup(
    name='mtorrentd',
    version='0.3.1',
    description='Search for and download multiple torrents at once',
    long_description='''Search for and download multiple torrents at once. Useful
                        when following a series and used in combination with chron and
                        torrent software which use watch folders (f.ex. rtorrent) to
                        automatically download series.''',
    url='https://github.com/arivarton/multi-torrent-downloader/',
    author='arivarton',
    author_email='packager@arivarton.com',
    license='GNU GPL v3',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Other Audience',
        'Topic :: Communications :: File Sharing',
        'Topic :: Utilities',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3 :: Only',
        'Operating System :: POSIX :: Linux',
    ],
    keywords='torrent download regex filter',
    install_requires=[
        'requests',
        'bs4',
        'pyyaml'
    ],
    python_requires='>=3',
    packages=find_packages(exclude=['tests',]),
    entry_points={
        'console_scripts': [
            'mtorrentd = mtorrentd.main:run',
        ]
    }
)