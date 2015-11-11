#!/usr/bin/env python3
# encoding=utf8
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals
from future.standard_library import install_aliases
install_aliases()
import sys
import blessings
from bs4 import BeautifulSoup

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

t = blessings.Terminal()

def main():
    url = "http://sentic.net/api/en/concept/"

    polar = float(0)
    i = 1
    while i<len(sys.argv):
        try:
            html = urlopen(url + sys.argv[i] + '/polarity')
            soup = BeautifulSoup(html.read(), "html.parser")
            for value in soup.find_all('polarity'):
                polar = polar + float(value.string)
            i = i + 1
        except:
            i = i + 1
    if polar > 0:
        print(t.green("✓"), t.cyan("This is a"), t.green("Positive"), t.cyan("sentence."))
        return
    print(t.red("✘"), t.cyan(" This is a"), t.red("Negative"), t.cyan("sentence."))
    return

main()
