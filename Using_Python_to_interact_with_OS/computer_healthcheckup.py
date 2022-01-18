#!/usr/bin/env python3 
import shutil
import psutil

def check_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free>20