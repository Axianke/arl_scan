import logging
import configparser
from arl.domain import output__ids
from arl.process_domain import extract
from setting import TOKEN

config = configparser.ConfigParser()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)



def start():
    name = input("请输入你的灯塔任务名称(如：资产侦查任务-test):")
    output__ids(TOKEN,name)

if __name__ == "__main__":
        start()
