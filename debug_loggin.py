import logging

logging.basicConfig(filename='example.log', level=logging.debug)

def add(a, b):
    logging.info("execution de la fonction add")
    logging.debug(a,b)
    if a>b and b>0:
        logging.debug("A et B sont positifs")
        return a+b

add(5,10)