import requests
from awvs.start_scan import start_scan
from setting import AWVS_URL, KEY
import urllib3
import json
urllib3.disable_warnings()
from urllib.parse import urljoin
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)






def add_target_to_awvs(target_url):
    target = urljoin(AWVS_URL, '/api/v1/targets/add')
    data = json.dumps({"targets": [{"address": target_url, "description": "ARL-AUTO"}], "groups": []})
    headers = {'Content-Type': 'application/json', "X-Auth": KEY}
    try:
        response = requests.post(target, data=data, headers=headers, timeout=30, verify=False)
        response.raise_for_status()
        target_id = response.json()['targets'][0]['target_id']
        if target_id:
            start_scan(target_id)
            logger.info(f"Successfully added target {target_url}")
    except Exception as e:
        logger.error(f"Failed to add target to AWVS: {e}")