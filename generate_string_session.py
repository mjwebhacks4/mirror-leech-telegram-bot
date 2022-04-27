from pyrogram import Client

API_KEY = 3796974
API_HASH = "9511d0112631f9990337eb724d1a7d0d"
with Client(api_id=API_KEY, api_hash=API_HASH, in_memory=True) as app:
    print(app.export_session_string())
