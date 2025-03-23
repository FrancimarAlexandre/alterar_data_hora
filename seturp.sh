#!/bin/bash

# Obtém o argumento passado pelo Python
MINHA_VARIAVEL=$1

# Verifica se a variável está vazia
if [ -z "$MINHA_VARIAVEL" ]; then
    echo "Erro: Nenhuma hora foi passada pelo script Python."
    exit 1
fi

# Desativar a sincronização automática do horário
sudo timedatectl set-ntp off

# Ajustar a hora manualmente
sudo timedatectl set-time "$MINHA_VARIAVEL"

# Reativar a sincronização automática
sudo timedatectl set-ntp on

echo "Hora ajustada para: $MINHA_VARIAVEL"
