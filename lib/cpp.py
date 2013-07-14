# -*- coding: utf-8 -*-

def readMeta():
    import yaml
    return yaml.load(open("solve.yaml"))

def profile(handler):
    #try:
    handler()
    #except Exception, e:
    #    pass

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
        meta = readMeta()
        lstring = " ".join(map(lambda e: "-l"+e, meta["libraries"]))
        template = "g++ -std=c++0x -g -O0 -Wall solve.cpp %s -o %s"
        command = template % (lstring, binaryPath)
        subprocess.check_call(command, shell=True)
    if os.path.exists("solve"):
        os.remove("solve")
    os.symlink(binaryPath, "solve")

def launch():
    profile(compile)
    import subprocess
    subprocess.check_call("./solve", shell=True)
