from setuptools import setup

setup(
    name="openeobs_config_generator",
    version="0.1",
    description="A tool for creating configurations for Open-eObs",
    author="Colin Wren",
    author_email="colin@gimpneek.com",
    url="http://github.com/NeovaHealth/demo-conf-generator",
    provides=["openeobs_config_generator"],
    packages=['configuration_generator'],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "new_openeobs_config = configuration_generator.__main__:main"
        ],
    },
    install_requires=['Jinja2>=2.7.3', 'CairoSVG==1.0.19', 'argparse>=1.4.0'],
    license="GPL",
    zip_safe=True,
)
