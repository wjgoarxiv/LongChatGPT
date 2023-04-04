from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="LongChatGPT",
    version="1.0.0",
    author="wjgoarxiv",
    author_email="woo_go@yahoo.com",
    description="A tool to throw long contents to ChatGPT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wjgoarxiv/longchatgpt",
    install_requires=[
        "pyfiglet",
        "tabulate",
        "PyPDF2",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires='>=3.7',
    packages=['LongChatGPT'],
    entry_points={
        'console_scripts': [
            'longchatgpt = LongChatGPT.__main__:main',
        ],
    },
)
