#!/usr/bin/env python

import pyndn as ndn
import os
import re
import sys
import argparse

parser = argparse.ArgumentParser(description='Fetch certificates and import them into NDNS')

parser.add_argument('file', metavar='file', type=str,
                    help='''Input file containing certificate names''')

args = parser.parse_args()

if (not args.file):
    parser.print_help()
    exit(1)

if args.file == "-":
  file = sys.stdin
else:
  file = open(args.file)

l = {}

for line in file:
  name = ndn.Name(line)
  key = str(name[:-1])
  if key not in l:
    l[key] = name
  else:
    if name[-1] > l[key][-1]:
      l[key] = name

for value in l.itervalues():
  zone = ndn.Name(re.sub(r'\/KEY.*$', '', str(value)))
  type = value[-2]
  label = value[len(zone) + 1:-2]

  print "%s (%s): %s %s" % (zone, value, type, label)

  os.system("ndns-remove-rr %s %s %s" % (zone, label, type))
  os.system("ndn-tlv-peek %s | base64 | ndns-add-rr-from-file %s -" % (value, zone))
