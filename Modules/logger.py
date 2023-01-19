import logging
import datetime

def logger_start():

    logging.basicConfig(filename=r'Piloto\Log\logs.log', level=logging.INFO)
    logging.info("Robô Iniciado - "+ str(datetime.datetime.now()))

def logger_add(mensagem,erro=True):
    
    if(erro):
        logging.info(str(mensagem)+"- "+ str(datetime.datetime.now()))

    else:
        logging.error(str(mensagem)+"- "+ str(datetime.datetime.now()))
