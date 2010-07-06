from distutils.core import setup

setup(name='mongol',
    version='0.1.0',
    description='Track your site\'s traffic and generate custom reports',
    long_description=open('README.rst').read(),
    author='Justin Quick',
    author_email='justquick@gmail.com',
    url='http://github.com/justquick/django-activity-stream',
    scripts=['bin/mongol-serve','bin/mongol-report'],
    install_requires=['pymongo'],
    classifiers=['Development Status :: 4 - Beta',
                 'Environment :: Web Environment',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Utilities'],
)
