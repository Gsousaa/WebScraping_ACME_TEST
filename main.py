from Modules import init_selenium as selenium
from Modules import save_csv as gera_csv
from Modules import extract as extrator
from Modules import login as login
from Modules import logger as log


if __name__ == "__main__":
    try:
        log.logger_start()
        log.logger_add("Inicializando o selenium")
        driver =  selenium.inicializa_selenium(log)
        log.logger_add("Realizando Login")
        login.login(driver,log)
        log.logger_add("Iniciado a extração dos dados")
        extrator.extract(driver,log)
        log.logger_add("Salvando dados em arquivo csv")
        gera_csv.table_to_csv(driver,log)
    
    except Exception as e:
        log.logger_add(e,True)