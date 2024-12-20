# APIWatchdog

## APIWatchdog

- APIWatchdog é uma automação em Python que monitora o status de APIs e envia notificações ao seu bot do Telegram quando uma API fica inoperante. O objetivo é alertar rapidamente sobre qualquer indisponibilidade, permitindo ações rápidas para restaurar o serviço.

## Funcionalidades

- Monitora APIs através de requisições periódicas.
- Verifica o status de resposta (HTTP status codes).
- Notifica via Telegram quando a API monitora está inoperante ou com problemas de conectividade.
- Fácil configuração para adicionar ou remover APIs monitoradas.

## Requisitos

- Python 3.x
- Pacotes Python:
- requests: para realizar as requisições HTTP às APIs.
- python-telegram-bot: para enviar as mensagens ao bot do Telegram.

## Uso

- Execute o script principal para iniciar o monitoramento:
- monitor_api.py