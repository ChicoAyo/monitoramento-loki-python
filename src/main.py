!pip install python-logging-loki

import logging
import logging_loki
import time
import random

# Configuração do Handler para o Loki
handler = logging_loki.LokiHandler(
    url="SUA URL GRAFANA/loki/api/v1/push",
    tags={"application": "projeto-resiliencia", "env": "prod"},
    auth=("SEU ID", "SEU TOKEN"),
    version="1",
)

logger = logging.getLogger("my-logger")
logger.addHandler(handler)

print("🚀 Iniciando envio de logs...")

# Loop para simular tráfego (Sucessos e Erros)
for i in range(100):
    if random.random() > 0.8: # 20% de chance de erro
        logger.error("Falha na conexão com banco de dados", extra={"status": "500"})
        print(f"Iteração {i}: Enviado ERRO 500")
    else:
        logger.info("Acesso à página principal", extra={"status": "200"})
        print(f"Iteração {i}: Enviado SUCESSO 200")

    time.sleep(1) # Espera 1 segundo entre logs
