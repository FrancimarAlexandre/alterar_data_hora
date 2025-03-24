import ntplib
from datetime import datetime
import pytz
import subprocess

def get_ntp_time(timezone):
    # Obter a hora UTC
    client = ntplib.NTPClient()
    response = client.request('pool.ntp.org')
    ntp_time = datetime.utcfromtimestamp(response.tx_time)  # Converte timestamp para datetime

    # Definir o fuso horário desejado
    local_timezone = pytz.timezone(timezone)
    local_time = ntp_time.replace(tzinfo=pytz.utc).astimezone(local_timezone)
    
    # Retornar hora formatada
    return local_time.strftime('%Y-%m-%d %H:%M:%S')

# Passando o fuso horário desejado (ex: 'America/Sao_Paulo')
valor = get_ntp_time('America/Sao_Paulo')
print(f"Hora obtida do NTP no fuso horário correto: {valor}")

# Chamar o script shell passando a variável como argumento
subprocess.run(["bash", "../seturp.sh", valor])
