import os
import requests

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
TEXT = os.getenv("TEXT", "").strip()

TAREFAS_FILE = "tarefas.txt"

def enviar(msg):
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )

if TEXT.startswith("/add"):
    tarefa = TEXT.replace("/add", "").strip()
    if tarefa:
        with open(TAREFAS_FILE, "a", encoding="utf-8") as f:
            f.write(tarefa + "\n")
        enviar(f"✅ Tarefa adicionada:\n{tarefa}")
    else:
        enviar("⚠️ Use assim:\n/add Comprar algo")

elif TEXT.startswith("/list"):
    if os.path.exists(TAREFAS_FILE):
        with open(TAREFAS_FILE, "r", encoding="utf-8") as f:
            tarefas = f.read().strip()
        if tarefas:
            enviar("📋 Suas tarefas:\n\n" + tarefas)
        else:
            enviar("📭 Lista vazia")
    else:
        enviar("📭 Lista vazia")

elif TEXT.startswith("/clear"):
    open(TAREFAS_FILE, "w", encoding="utf-8").close()
    enviar("🧹 Todas as tarefas foram removidas")

else:
    enviar(
        "🤖 Comandos disponíveis:\n"
        "/add <tarefa>\n"
        "/list\n"
        "/clear"
    )
