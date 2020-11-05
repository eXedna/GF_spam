import os
import sys

from LogPython import LogManager; LogManager = LogManager()

def run_python_tool(command):
    os.system(
        'cd \"' + os.path.dirname(sys.executable) + '\" && ' + os.path.basename(sys.executable) + ' -m ' + command)
    
run_python_tool("pip install --upgrade pip")
run_python_tool('pip install click bs4 requests --user')

LogManager.info("Successfully installed => go to hacking :)")