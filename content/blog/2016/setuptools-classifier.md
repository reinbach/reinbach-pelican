Title: Setuptools - upload error with Python 3.5
Date: 2016-10-13
Tags: python3.5 setuptools
Slug: setuptools-classifiers-upload-python3-5
Author: Greg Reinbach

Came across a funky error attempting to upload a package to PyPi using Python 3.5

    $ python setup.py sdist bdist_wheel upload

    ...

    Traceback (most recent call last):
      File "setup.py", line 45, in <module>
        install_requires=['django>=1.10']
      File "/usr/lib64/python3.5/distutils/core.py", line 148, in setup
        dist.run_commands()
      File "/usr/lib64/python3.5/distutils/dist.py", line 955, in run_commands
        self.run_command(cmd)
      File "/usr/lib64/python3.5/distutils/dist.py", line 974, in run_command
        cmd_obj.run()
      File "/usr/lib64/python3.5/distutils/command/upload.py", line 63, in run
        self.upload_file(command, pyversion, filename)
      File "/usr/lib64/python3.5/distutils/command/upload.py", line 162, in upload_file
        body.write(value)
    TypeError: a bytes-like object is required, not 'str'

The `setup.py` file was along these lines

    #!python
    setup(
        name='project-name',
        ...
        platforms=['any'],
        license='MIT License',
        classifiers=(
            'Environment :: Web Environment',
            'Framework :: Django',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.5',
        ),
        packages=find_packages(),
        install_requires=['django>=1.10']
    )

Took me a while to figure out what the issue was, and why the error, but alas is appears that the `classifiers` needs to be a list and not a tuple.

So changing the `setup.py` file to something like this

    #!python
    setup(
        name='project-name',
        ...
        platforms=['any'],
        license='MIT License',
        classifiers=[
            'Environment :: Web Environment',
            'Framework :: Django',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.5',
        ],
        packages=find_packages(),
        install_requires=['django>=1.10']
    )

Fixed the issue.
