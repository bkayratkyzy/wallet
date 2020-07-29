from constants import *
import subprocess
import os
from dotenv import load_dotenv
import bit
import web3
from bit import Key
from web3 import Web3
from eth_account import Account
from pathlib import Path
from getpass import getpass
import json

command = './derive -g --mnemonic="raise tiger knee race abuse clarify glue any pledge pen side trip"

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
p_status = p.wait()

print(output)

mnemonic = os.getenv('MNEMONIC', 'raise tiger knee race abuse clarify glue any pledge pen side trip')