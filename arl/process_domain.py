from concurrent.futures import ThreadPoolExecutor
import re
import threading
import logging
from awvs.addto_awvs import add_target_to_awvs
from setting import VULN
from vuln.vuln import send_get_vuln


# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 创建锁
lock = threading.Lock()

# 预编译正则表达式
pattern = re.compile(r'^(https?):\/\/([a-zA-Z0-9.-]+\.[a-zA-Z]{2,}|([0-9]{1,3}\.){3}[0-9]{1,3})(:\d+)?')


def extract(domains):
    with ThreadPoolExecutor(max_workers=10) as executor:  # max_workers 可根据需要调整
        executor.map(process_domain, domains)

def process_domain(domain):
    match = pattern.match(domain)
    if match:
        target_url = match.group(0)
        with lock:
            print(target_url)
            try:
                if VULN =="yes":  
                    send_get_vuln(target_url)
                if VULN =="no":
                    add_target_to_awvs(target_url)
            except Exception as e:
                logger.error(f"Failed to process {target_url}: {e}")
    else:
        with lock:
            logger.warning(f"No match found for domain: {domain}")
