import requests
import logging
import urllib3
urllib3.disable_warnings() # type: ignore # 屏蔽证书警告
from setting import PROXY_SERVER
# 代理配置
proxies = {
    'http': f'http://{PROXY_SERVER}',
    'https': f'http://{PROXY_SERVER}'
}

# 日志配置
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def send_get_vuln(url):
    try:
        response = requests.get(url, proxies=proxies,verify=False)
        logger.info(f"Response from {url}: {response.status_code}")
        return response
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to send request to {url}: {e}")
        return None