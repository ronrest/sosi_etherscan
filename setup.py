import setuptools

setuptools.setup(
    name="sosi_etherscan",
    version="0.0.1",
    author="ronny",
    description='Something',
    url="https://github.com/ronrest/sosi_etherscan",
    project_urls={
        "Bug Tracker": "https://github.com/ronrest/sosi_etherscan/issues",
        "Documentation": "https://github.com/ronrest/sosi_etherscan/blob/master/README.md",
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        'Development Status :: Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8, <4.0",
    packages=setuptools.find_packages(),
    install_requires=[
        'python-dateutil',
        'python-decouple',
        'requests',
        'sosi-api==0.0.*',
    ],
    extras_require={
        'dev': [
            'pip-tools',
            'pylint',
            'pytest',
            'yapf',
        ]
    },
)