import sys
from os import environ

COMMAND_HANDLER = environ.get("COMMAND_HANDLER", "! /").split()
