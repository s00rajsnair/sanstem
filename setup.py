from setuptools import setup
import pathlib

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
  name="sanstem",
  version="0.0.7",
  author="Sooraj S Nair",
  author_email="soorajsnair@am.students.amrita.edu",
  description=("A rule-based stemmer for Sanskrit Verbs and Nouns'"),
  license="MIT",
  keywords="Sanskrit Stemmer",
  url="https://github.com/sooraj-nair/sanstem",
  packages=['sanstem'],
  long_description=README,
  install_requires=[            # I get to this in a second
          'devatrans',
          'polyglot',
  ],
  include_package_Data=True,
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
