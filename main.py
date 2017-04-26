import os
import sys
import time
import threading
import Patient
import Kensa
import setting
import DBControler
import pyodbc

from logging import getLogger
logger = getLogger(__name__)

if __name__ == "__main__":
    logger.info("Start")
    logger.info("Chack Already Exists Controlevr Process")
    # file cheak
    logger.info(os.getcwd() + "\PROC")

    pt = Patient.Patient()

    while 1:
        w_all_status = DBControler.get_status_db(type="ALL")
        w_pt_status = DBControler.get_status_db(type="Patient")

        if w_all_status == "READY":
            logger.info("ALL Start")
            if w_pt_status == "READY":
                DBControler.set_status_db(type="Patient", status="RUNNING")
                try :
                    pt.start()
                    logger.info("Pt Start")
                except RuntimeError:
                    logger.info("ERR")
            else:
                skip
        else:
            break

        time.sleep(3)

    DBControler.set_status_db(type="ALL", status="RUNNING")
