from setuptools import setup

setup(
    name="ptpl-transcoder",
    version="1.0.1",
    py_modules=["transcoder"],
    entry_points={
        "console_scripts": [
            "ptpl-transcoder=transcoder:main",
        ],
    },
    install_requires=[
        "lxml",
    ],
    description="A CLI tool to to decode .ptpl files into .xml and encode .xml files back into .ptpl format.",
    author="KRW CLASSIC",
    author_email="classic.krw@gmail.com",
    url="https://github.com/KRWCLASSIC/PTPL-CLI-Transcoder",
)
