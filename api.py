from passeo import passeo
import logging

# logger = logging.getLogger("python_observability")
logger = logging.getLogger(__name__)

# This is the task we want to run
def generate(times):
    """
    This function uses passeo to generate a password
    """
    logging.warning('here we go...')
    for x in range(times):
        logging.warning("generate something %s times", x)
        passeo().generate(length=10, numbers=True, symbols=True, uppercase=True, lowercase=False, space=True)

def check_strength():
    """
    This function uses passeo to check the strength of a password
    """
    logging.warning("Strenth check")
    passeo().strengthcheck("Passeo")
