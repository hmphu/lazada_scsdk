from setuptools import setup

setup(
    name="lazada_scsdk",
    version="0.1.0",
    description="Lazada Seller Center SDK",
    url="https://github.com/hmphu",
    author="hmphu",
    author_email="me@hmphu.com",
    license="MIT",
    install_requires=["requests"],
    include_package_data=True,
    package_dir={'lazada_scsdk': 'lazada_scsdk', 'lazada_scsdk.resources': 'lazada_scsdk/resources', 'lazada_scsdk.requests': 'lazada_scsdk/requests'},
    packages=['lazada_scsdk', 'lazada_scsdk.resources', 'lazada_scsdk.requests'],
    keywords='lazada seller center sdk',
    classifiers=[
        "Development Status :: 1 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
