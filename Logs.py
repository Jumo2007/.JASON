import logging
import os

if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(
    filename="logs/eventos.log",
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)


def log_info(mensaje):
    logging.info(mensaje)

def log_error(mensaje):
    logging.error(mensaje)
