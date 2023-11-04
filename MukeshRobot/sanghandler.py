import sys
from os import environ

import dotenv

COMMAND_HANDLER = environ.get("COMMAND_HANDLER", "! /").split()
