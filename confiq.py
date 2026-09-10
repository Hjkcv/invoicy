# === KONFIGURASI BOT ===
# Bisa diisi 2 cara:
# A) Kalau jalan di laptop/PC sendiri: langsung ganti nilai default di bawah ini
# B) Kalau di-deploy ke hosting (Railway/Render dkk): isi lewat "Environment Variables"
#    di dashboard hosting, dengan nama BOT_TOKEN dan ALLOWED_USER_IDS — kode ini akan
#    otomatis membacanya, tidak perlu edit file.

import os

# 1. Token bot dari @BotFather di Telegram
BOT_TOKEN = os.environ.get("BOT_TOKEN", "PASTE_TOKEN_DARI_BOTFATHER_DI_SINI")

# 2. Telegram user ID kamu (cek lewat @userinfobot di Telegram, kirim /start ke dia)
#    Kalau lewat Environment Variables, isi dipisah koma: 123456789,987654321
_default_ids = "123456789"
ALLOWED_USER_IDS = [
    int(uid.strip())
    for uid in os.environ.get("ALLOWED_USER_IDS", _default_ids).split(",")
    if uid.strip()
]

# Nama file database SQLite (otomatis dibuat saat bot pertama kali jalan)
DB_NAME = "invoices.db"