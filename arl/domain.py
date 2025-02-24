import json
import threading
import time
from urllib.parse import urljoin
import logging
import requests
from arl.process_domain import extract
from setting import SIZE, URL
import urllib3

lock = threading.Lock()  # 创建一个全局锁对象
urllib3.disable_warnings()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


seen_ids = set()  # 用于存储已处理过的ID

def output__ids(token, name):
    while True:

        target = urljoin(URL, 'api/task/')
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_10_1 rv:4.0; OC) AppleWebKit/532.1.1 (KHTML, like Gecko) Version/5.1.5 Safari/532.1.1',
            'Content-Type': 'application/json; charset=UTF-8',
            'Token': token
        }

        try:
            response = requests.get(target, headers=headers, params={'name': name, 'page': 1, 'size': SIZE}, timeout=30, verify=False)
            response.raise_for_status()
            asset_ids = [task['_id'] for task in response.json()['items'] if task['status'] == 'done']

            with lock:
                new_asset_ids = [asset_id for asset_id in asset_ids if asset_id not in seen_ids]
                seen_ids.update(new_asset_ids)  # 确保第一次获取的所有ID都被记录

            if new_asset_ids:
                extract(output_domain(new_asset_ids, headers))
            else:
                logger.info("No new tasks found. Sleeping for 5 minutes.")
                time.sleep(300)  # 休眠5分钟
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Request error during output: {e}")

def output_domain(new_asset_ids,headers):
    try:
        data = json.dumps({"task_id": new_asset_ids})
        response = requests.post(URL + '/api/batch_export/site/', data=data, headers=headers, timeout=30, verify=False)
        response.raise_for_status()
        logger.info("Data exported successfully")
        return response.text.split()
    except requests.exceptions.RequestException as e:
        logger.error(f"Request error during output: {e}")
