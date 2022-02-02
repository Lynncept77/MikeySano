@echo off
TITLE MikeyBot
:: Enables virtual env mode and then starts mikey
env\scripts\activate.bat && py -m MikeyBot
