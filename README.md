# bsr-metadata
Metadata files for BSR receiver software

# Why mirror?
The origin sites filter downloads from non-US networks, use older protocols,
or they do not provide HTTPS.

# Original file locations
The original files are available from the following locations:

http://celestrak.com/NORAD/elements/geo.txt
https://hpiers.obspm.fr/iers/bul/bulc/Leap_Second.dat
http://maia.usno.navy.mil/ser7/deltat.preds
http://maia.usno.navy.mil/ser7/deltat.data
ftp://ssd.jpl.nasa.gov/pub/eph/planets/de421.bsp

# Update mirror
A simple HTTP downloader is included in this repository. It will fetch and
cache the data into the mirror/ directory:

```
python fetch-metadata.py
```

