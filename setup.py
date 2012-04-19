from setuptools import setup
import os.path


try:
    # add classifiers and download_url syntax to distutils
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None
except:
    pass




setup(
    name='pyLingr',
    zip_safe=False,
    version='0.0.1',
    url='https://github.com/bgnori/pyLingr',
    py_modules=['pylingr'],
    provides=['pyLingr'],
)

