import io
from setuptools import setup, find_packages


def requirements(filename):
    reqs = list()
    with io.open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            yield line.strip()


setup(
    name='daa_api',
    version='1.0',
    packages=find_packages(),
    url="https://github.com/DavidSanSan110",
    author='David Sánchez Sánchez',
    author_email='davidsansan@usal',
    description='',
    long_description_content_type='text/markdown',
    install_requires=requirements(filename='requirements.txt'),
    data_files=[],
    entry_points={
        'console_scripts': [
            'daa_api=daa_api.run:main'
        ],
    },
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Developers"
    ],
    python_requires='>=3',
    project_urls={
        'Bug Reports': 'https://github.com/DavidSanSan110',
        'Source': 'https://github.com/DavidSanSan110',
    },
)