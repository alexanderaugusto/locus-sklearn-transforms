from setuptools import setup

setup(
    name='locus_deploy_transforms',
    version='1.0',
    description='''
            This is a sample python package for encapsulating custom
            tranforms from scikit-learn into Watson Machine Learning
      ''',
    url='https://github.com/alexanderaugusto/locus-deploy-transforms/',
    author='Alexander Augusto',
    author_email='alexaasf1010@gmail.com',
    license='BSD',
    packages=[
        'locus_deploy_transforms'
    ],
    zip_safe=False
)
