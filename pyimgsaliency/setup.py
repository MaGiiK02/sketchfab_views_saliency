from setuptools import setup

setup(name='pyimgsaliency',
      version='0.1',
      description='A package for calculating image saliency',
      url='https://github.com/yhenon/pyimgsaliency',
      author='Yann Henon',
      author_email='none',
      license='Apache',
      install_requires=['sklearn', 'opencv-python', 'networkx', 'numpy', 'scipy', 'scikit-image'],
      packages=['pyimgsaliency'],
      zip_safe=False)
