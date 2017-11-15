#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import os

def fetch_metadata():
    headers = {b'User-Agent': "bsr".encode()}
    urls = ["http://celestrak.com/NORAD/elements/geo.txt",
	    "https://hpiers.obspm.fr/iers/bul/bulc/Leap_Second.dat",
	    "http://maia.usno.navy.mil/ser7/deltat.preds",
	    "http://maia.usno.navy.mil/ser7/deltat.data",
	    "ftp://ssd.jpl.nasa.gov/pub/eph/planets/de421.bsp"
	    ]
    out_dir = "mirror/"
    for url in urls:
	f_name = "{0}{1}".format(out_dir, os.path.basename(url).split("/").pop())
	print("fetching {0} to {1}".format(url, f_name))
        r = urllib2.Request(url, None, headers)
	a = urllib2.urlopen(r)
	f = open(f_name, 'wb')
	f.write(a.read())

if __name__ == "__main__":
    fetch_metadata()
