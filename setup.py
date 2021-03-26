from setuptools import setup


with open('README.md', 'r') as description:
    long_description = description.read()

setup(
    name='markdown-alerts',
    version='0.1',
    author='gd',
    description='Python-Markdown Admonition alternative.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gitea.gch.icu/gd/markdown-alerts/',
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: The Unlicense (Unlicense)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=['markdown_alerts'],
    install_requires = ['markdown>=3.0'],
)
