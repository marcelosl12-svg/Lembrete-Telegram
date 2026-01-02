import requests
from datetime import datetime

TOKEN = "7399101240:AAEHmk41Q4UPubjd-5YMYzpwVgtfk5lDLgk"
CHAT_ID = "996780641"

with open("tarefas.txt", "r", encoding="utf-8") as f:
    tarefas = f.read()

mensagem = f"📅 *Tarefas para amanhã ({datetime.now().strftime('%d/%m')})*\n\n"
for linha in tarefas.splitlines():
    if linha.strip():
        mensagem += f"✔ {linha}\n"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": mensagem,
    "parse_mode": "Markdown"
})
