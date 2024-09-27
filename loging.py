import logging
from datetime import datetime


logfile = f'{datetime.now().strftime("%H_%M_%S.%d_%m_%Y")}.log'

game_logger = logging.getLogger("my_log")
game_logger.setLevel(logging.INFO)
FH = logging.FileHandler(logfile)
basic_formater = logging.Formatter('%(message)s')
FH.setFormatter(basic_formater)
game_logger.addHandler(FH)
