import logging

logging.basicConfig(filename="mylog.txt", level=logging.INFO)
log = logging.getLogger(name="MyFirstLog")
help(log)

log.debug("Phew, made it through.")
log.error("Something is very wrong!")
log.info("This is just FYI.")
