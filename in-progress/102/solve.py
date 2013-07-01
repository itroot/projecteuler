#!/usr/bin/env python
# -*- coding: utf-8 -*-

def compile():
    import subprocess
    import os
    secretPath = ".pycpplauncher"
    if not os.path.exists(secretPath):
        os.mkdir(secretPath)
    data = open("solve.cpp").read()
    import hashlib
    sha1 = hashlib.sha1()
    sha1.update(data)
    digest = sha1.hexdigest()
    binaryPath = secretPath+"/"+digest
    if (not os.path.exists(secretPath+"/"+digest)):
        subprocess.check_call("g++ -g -O0 -Wall solve.cpp -o %s" % binaryPath, shell=True)
    os.remove("solve")
    os.symlink(binaryPath, "solve")

def launch():
    import subprocess
    subprocess.check_call("./solve", shell=True)

def loadCpp():
    compile()
    launch()

loadCpp()
