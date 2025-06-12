from setuptools import setup, find_packages
import os

# Read the contents of your README file
with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='academy-tester',  # This is the name your package will be installed as
    version='0.1.0',  # Start with 0.1.0 and increment for releases
    author='Alastair Thomson',
    author_email='alastairw.thomson@gmail.com',
    description='Helps test Python Programs while using the "JetBrains Academy" plug on PyCharm',
    long_description=long_description,
    long_description_content_type='text/markdown',  # Specify the content type of the long description
    url='https://github.com/yourusername/your-package-name',  # URL to your project's repository
    packages=find_packages(),  # Automatically finds all packages in the current directory
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.0',  # Minimum Python version required
    install_requires=[
        # List your project dependencies here. Example:
        # 'requests>=2.20.0',
        # 'numpy',
    ],
    # You can also include data files, if needed. Example:
    # include_package_data=True,
    # package_data={
    #     'your_package_name': ['data/*.txt'],
    # },
    # For command-line scripts:
    # entry_points={
    #     'console_scripts': [
    #         'your_command=your_package_name.main:main_function',
    #     ],
    # },
)
