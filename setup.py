from distutils.core import setup
setup(
  name = 'heapy',
  packages = ['heapy'], # this must be the same as the name above
  version = '0.5',
  description = 'An priority queue built with an in-place modifiable binary heap',
  author = 'Waylon Flinn',
  author_email = 'waylonflinn@gmail.com',
  url = 'https://github.com/waylonflinn/heapy', # use the URL to the github repo
  download_url = 'https://github.com/peterldowns/mypackage/tarball/0.1', # I'll explain this in a second
  keywords = ['heap', 'priority queue', 'decrease-key', 'increase-key', 'dijkstra', 'rolling median'], # arbitrary keywords
  classifiers = [],
)
