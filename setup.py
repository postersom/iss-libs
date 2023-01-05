from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='iss-libs',  # How you named your package folder (MyLib)
    version='0.0.5',  # Start with a small number and increase it with every change you make
    author='Somsak Binyaranee',  # Type in your name
    author_email='poster.som@gmail.com',  # Type in your E-Mail
    description='',  # Give a short description about your library
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/postersom/iss-libs',  # Provide either the link to your github or to your website
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    packages=find_packages(),
    package_dir={'client': 'Client'},
    install_requires=['connexion',
                      'Flask',
                      'Flask-SocketIO',
                      'marshmallow',
                      'marshmallow_sqlalchemy',
                      'matplotlib',
                      'paramiko',
                      'prettytable',
                      'psutil',
                      'python-dotenv',
                      'python-gitlab',
                      'redis',
                      'robotframework',
                      'six',
                      'sqlalchemy',
                      'swagger-ui-bundle',
                      'xmltodict'],
    classifiers=[
        'Development Status :: 4 - Beta',   # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 3.9',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
