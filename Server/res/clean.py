#!/usr/bin/env python3
#-*-coding:utf-8 -*-

import subprocess

subprocess.call('rm -f /conf/session.dat'.split(), shell=False)
subprocess.call('touch /conf/session.dat'.split(), shell=False)
subprocess.call('rm -f /data/downloads/*', shell=True)
print('data cleared')