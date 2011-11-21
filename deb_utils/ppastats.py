#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GPL v3
# Written by arand
# Inspired by Alex Mandel's script snippets at https://bugs.launchpad.net/launchpad/+bug/139855
# This is my biggest project in python to date, it is KLUDGE beyond imagination.
# On Debian-like systems the package python-launchpadlib is required

import sys
import os
from launchpadlib.launchpad import Launchpad

archs = ["i386", "amd64"]
releases = ["hardy", "lucid", "maverick", "natty", "oneiric"]

if len(sys.argv) < 3: print "Usage: ppastats owner ppaname1 [ppaname2 ...]"

owner_name = sys.argv[1]
ppas = sys.argv[2:]

for individual_ppa in ppas:
	print "usage stats for PPA with owner \"" + owner_name + "\" named \"" + individual_ppa + "\""
	print "#####"
	cachedir = os.path.expanduser("~/.launchpadlib/cache/")

	launchpad = Launchpad.login_anonymously('ppastats', 'production', cachedir, version='devel')
	owner = launchpad.people[owner_name]
	archive = owner.getPPAByName(name=individual_ppa)

	for individual_arch in archs:
		for individual_release in releases:
			individual_distro_arch_series = "https://api.launchpad.net/devel/ubuntu/" + individual_release + "/" + individual_arch
			print "\t" + individual_release + "/" + individual_arch + ":"
			for individual_archive in archive.getPublishedBinaries(status='Published',distro_arch_series=individual_distro_arch_series):
				print individual_archive.binary_package_name + "\t" + individual_archive.binary_package_version + "\t" + str(individual_archive.getDownloadCount())
	print "#####"
