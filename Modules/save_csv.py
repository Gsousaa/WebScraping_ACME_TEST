from bs4 import BeautifulSoup
import pandas as pd
import re
import csv


def table_to_csv(driver,log):
    try:
        page_source = driver.page_source
        soup = BeautifulSoup(page_source,'lxml')
        matches = []
        for child in soup.find_all('table')[0].children:
            for td in child:
                regex = re.findall(">.*<",str(td),re.MULTILINE)
                if(regex == "\n" or str(td).__contains__('<tr>\n<td>')):
                    regex = re.findall(".*\w.*\n ",str(td),re.MULTILINE)
                regex = re.sub(r">|<|'|[[]|[]]|'<td>\n '|                       |\\n |td","",str(regex),0,re.MULTILINE).split(", ") 
                regex = list(filter(None, regex))
                if(not td =="\n"):

                    matches.append(regex)
        
        with open(r'Piloto\Files\teste.csv', 'w',newline='') as f:
        
            write = csv.writer(f)
            write.writerows(matches)
            
        
            
    except Exception as e:
        log.logger_add(e,True)