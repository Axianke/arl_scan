import configparser
import requests
from setting import AWVS_URL, KEY, SCAN_SPEED, LIMIT_CRAWLER_SCOPE, PROXY_SERVER, PROXY_ENABLED
import urllib3
import json
from urllib.parse import urljoin
urllib3.disable_warnings()
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def start_scan(target_id):
    target = urljoin(AWVS_URL, '/api/v1/scans')
    headers = {'Content-Type': 'application/json', "X-Auth": KEY}
    profile_id = "11111111-1111-1111-1111-111111111111" if  PROXY_ENABLED == 'False' else "11111111-1111-1111-1111-111111111117"
    
    try:
        configuration(target_id, profile_id)
        scan_data = {
            "target_id": target_id,
            "profile_id": profile_id,
            "incremental": False,
            "schedule": {"disable": False, "start_date": None, "time_sensitive": False}
        }
        response = requests.post(target, json=scan_data, headers=headers, timeout=30, verify=False)
        response.raise_for_status()
        logger.info("Scan task started successfully")
    except Exception as e:
        logger.error(f"Failed to start scan task: {e}")

def configuration(target_id, default_scanning_profile_id):
    headers = {'Content-Type': 'application/json', "X-Auth": KEY}
    configuration_url = urljoin(AWVS_URL, f'/api/v1/targets/{target_id}/configuration')

    data = {
        "scan_speed": SCAN_SPEED,
        "login": {"kind": "none"},
        "ssh_credentials": {"kind": "none"},
        "default_scanning_profile_id": default_scanning_profile_id,
        "sensor": False,
        "user_agent": 'User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
        "case_sensitive": "auto",
        "limit_crawler_scope": LIMIT_CRAWLER_SCOPE,
        "excluded_paths": [],
        "authentication": {"enabled": False},
        "proxy": {"enabled": PROXY_ENABLED, "protocol": "http", "address": PROXY_SERVER.split(':')[0], "port": PROXY_SERVER.split(':')[1]},
        "technologies": [],
        "custom_headers": [],
        "custom_cookies": [],
        "debug": False,
        "client_certificate_password": "",
        "issue_tracker_id": "",
        "excluded_hours_id": ""
    }

    try:
        r = requests.patch(url=configuration_url, data=json.dumps(data), headers=headers, timeout=30, verify=False)
        logger.info(f"Configuration applied to target {target_id}")
    except Exception as e:
        logger.error(f"Failed to configure target {target_id}: {e}")