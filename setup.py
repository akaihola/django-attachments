from distutils.core import setup
import glob

data = [ "locale/" + l.rsplit('/')[-1]+"/LC_MESSAGES/*.*"
         for l in glob.glob("attachments/locale/*.?o")]
data.append('templates/attachments/*.html')

setup(
    name='django-attachments',
    version=__import__('attachments').__version__,
    description='A generic attachment framework for Django',
    author='Chicago Django user group and Antti Kaihola',
    author_email='akaihol+django@ambitone.com',
    url='http://github.com/akaihola/django-attachments',
    packages=[
        'attachments',
        'attachments.templatetags',
    ],
    package_data={'attachments': data},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Programming Language :: Python :: 2.3',
        'Programming Language :: JavaScript',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ]
)
