from pypresence import Presence
import time

# Discord RPC connection and parameters
client_id = "842745089696596010"
image = "plex"
large_text = "Plex Media Server"
small = "github"
small_text = "Github: Plex-Rich-Presence"
RPC = Presence(client_id)
RPC.connect()

def update():
    details = "En pause..."
    timer = int(time.time())
    is_idling = 1