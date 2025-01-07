# APIWatchdog

<p align="center">
  <img src="https://i.imgur.com/U7Lgfls.png" alt="GIF" width="300" height="200">
</p>

## APIWatchdog

- APIWatchdog é uma automação em Python que monitora o status de APIs e envia notificações ao seu bot do Telegram quando uma API fica inoperante. O objetivo é alertar rapidamente sobre qualquer indisponibilidade, permitindo ações rápidas para restaurar o serviço.
-Este projeto implementa uma automação em Python para monitorar a disponibilidade de APIs e enviar notificações via Telegram quando uma API monitorada está inoperante. A integração com o Telegram é feita utilizando um bot configurado pelo BotFather.

## Funcionalidades

- Monitora APIs através de requisições periódicas.
- Verifica o status de resposta (HTTP status codes).
- Notifica via Telegram quando a API monitora está inoperante ou com problemas de conectividade.
- Fácil configuração para adicionar ou remover APIs monitoradas.

## Configuração

1. Criar um Bot no Telegram
- Você precisa de um token de acesso ao bot do Telegram, que pode ser obtido seguindo estes passos:
Abra o aplicativo do Telegram e procure por BotFather.
Inicie uma conversa com o BotFather e use o comando /newbot para criar um novo bot.
Siga as instruções para dar um nome e um identificador ao bot.
O BotFather fornecerá um token de API. Esse token será usado para autenticar o seu bot. Mantenha esse token seguro.

2. Configurar o Token do Bot e IDs
No arquivo monitor_api.py, adicione as seguintes informações:

TOKEN: O token do bot fornecido pelo BotFather.
CHAT_ID: O ID do chat ou grupo do Telegram onde as notificações serão enviadas.

# monitor_api.py

`TOKEN = 'seu_token_aqui'`
`CHAT_ID = 'seu_chat_id_aqui'`

3. Adicionar URLs de APIs para Monitoramento
No arquivo monitor.py, configure as URLs das APIs que você deseja monitorar:

# monitor_api.py

`API_URLS = [`
   ` 'https://api1.example.com/health',`
   ` 'https://api2.example.com/status']`


## Requisitos

- Python 3.x
- Pacotes Python:
- requests: para realizar as requisições HTTP às APIs.
- python-telegram-bot: para enviar as mensagens ao bot do Telegram.

## Uso

- Execute o script principal para iniciar o monitoramento:
- monitor_api.py
