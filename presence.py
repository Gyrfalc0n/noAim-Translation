from pypresence import Presence
import time

# Discord RPC connection and parameters
client_id = "975673805160710174"
image = "logo"
large_text = "noAim Translator"
small = "small"
small_text = "noaim.eu"
base_timer = int(time.time())
RPC = Presence(client_id)
RPC.connect()

def presence_update(state, details):
    if details == "null":
        details = "Idling..."
    if state != "null":
        RPC.update(state=state,
                details=details,
                large_image=image,
                large_text=large_text,
                small_image=small,
                small_text=small_text,
                start=base_timer)
    else:
        RPC.update(details=details,
                large_image=image,
                large_text=large_text,
                small_image=small,
                small_text=small_text,
                start=base_timer)