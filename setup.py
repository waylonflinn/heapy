from distutils.core import setup

# read the contents of README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
  name = 'heapy',
  packages = ['heapy'], # this must be the same as the name above
  version = '0.7',
  description = 'A priority queue built with an in-place modifiable binary heap',
  author = 'Waylon Flinn',
  author_email = 'waylonflinn@gmail.com',
  url = 'https://github.com/waylonflinn/heapy', # use the URL to the github repo
  keywords = ['heap', 'priority queue', 'decrease-key', 'increase-key', 'dijkstra', 'rolling median', 'remove'], # arbitrary keywords
  classifiers = [],
  long_description=long_description,
  long_description_content_type='text/markdown',
)
