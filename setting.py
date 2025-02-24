import configparser

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')
TOKEN = config.get('login', 'key').strip("'")
SIZE = config.get('size', 'size').strip("'")
URL = config.get('url', 'url').strip("'")
KEY = config.get('awvs', 'key').strip("'")
AWVS_URL = config.get('awvs', 'awvs_url').strip("'")
SCAN_SPEED = config.get('scan_seting', 'scan_speed').strip("'")
LIMIT_CRAWLER_SCOPE = config.get('scan_seting', 'limit_crawler_scope').strip("'")
PROXY_ENABLED = config.get('scan_seting', 'proxy_enabled').strip("'")
PROXY_SERVER = config.get('scan_seting', 'proxy_server').strip("'")
VULN = config.get('scan_seting', 'vuln').strip("'")