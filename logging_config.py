import logging

# configurare logare
logging.basicConfig(
    filename='automation_log.log',  # fisierul de log
    level=logging.DEBUG,  # captura toate log-urile de la nivelul DEBUG in sus
    format='%(asctime)s - %(levelname)s - %(message)s',  # formatul intrarii in log
    filemode='w'  # 'w' pentru a suprascrie fisierul de log de fiecare data, 'a' pentru a adauga la final
)

def log_message(message):
    """log mesajele personalizate"""
    logging.info(message)

def log_error(message):
    """log mesajele de eroare"""
    logging.error(message)

def log_warning(message):
    """log mesajele de avertizare"""
    logging.warning(message)

def log_debug(message):
    """log mesajele de debug"""
    logging.debug(message)
