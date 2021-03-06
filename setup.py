from distutils.core import setup, Extension

setup(
    name='misaka',
    version='0.4.0',
    description='A Python binding for Sundown.',
    author='Frank Smit',
    author_email='frank@61924.nl',
    url='http://misaka.61924.nl/',
    license='MIT',
    long_description=open('README.txt').read(),
    ext_modules=[Extension('misaka', [
        'src/misaka.c',
        'src/sundown/array.c',
        'src/sundown/buffer.c',
        'src/sundown/markdown.c',
        'src/sundown/html.c',
        'src/sundown/html_smartypants.c',
        'src/sundown/autolink.c'
    ])]
)
