from setuptools import setup


setup(
    name="lol",
    version="0.1",
    py_modules=["lol"],
    install_requires=[
        'Click'
    ],
    entry_points="""
        [console_scripts]
        lol=lol:cli
    """,
)
