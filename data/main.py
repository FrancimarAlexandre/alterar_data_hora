import ntplib
from datetime import datetime
import time

def get_ntp_time():
    client = ntplib.NTPClient()
    response = client.request('pool.ntp.org')
    ntp_time = datetime.utcfromtimestamp(response.tx_time)  # Converte timestamp para datetime
    return ntp_time.strftime('%Y-%m-%d %H:%M:%S')

print(get_ntp_time())
