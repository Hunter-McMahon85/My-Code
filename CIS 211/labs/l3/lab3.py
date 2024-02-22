import logging

# logging module allows for the organization of diagnostic output: debugging, info, warning, or error messages.
# creating a logging object:

logging.basicConfig()
# to save the log to a text file:
# logging.basicConfig(filename = "log.txt", level = logging.INFO)

log = logging.getLogger(name = "MyFirstLog")

# five predefined severity levels:
# CRITICAL	50
# ERROR	    40
# WARNING	30
# INFO	    20
# DEBUG	    10
# You can specify any level with the log.log() method.

