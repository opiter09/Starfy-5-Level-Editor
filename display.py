import tcod
import sys
import os
import math

WIDTH, HEIGHT = int(sys.argv[2], 16), int(sys.argv[3], 16)  # Console width and height in tiles.

# Load the font, a 32 by 8 tile font with libtcod's old character layout.
tileset = tcod.tileset.load_tilesheet("dejavu16x16_gs_tc.png", 512//16, 128//16, tcod.tileset.CHARMAP_TCOD)
# Create the main console.
console = tcod.Console(WIDTH, HEIGHT, order = "F")
# Create a window based on this console and tileset.
context = tcod.context.new(columns = console.width, rows = console.height, tileset = tileset)
for root, dirs, files in os.walk("./" + sys.argv[1]):
    for file in files:
        reading = open(os.path.join(root, file), "rb")
        whole = reading.read()
        reading.close()
        console.print(x = math.ceil(int.from_bytes(whole[0:2], "little") / 16), y = math.ceil(int.from_bytes(whole[2:4], "little") / 16),
            string = chr(int.from_bytes(whole[4:6], "little") + ord("0")))
        print(chr(int.from_bytes(whole[4:6], "little") + ord("0")) + " = " + str.format("{:02X}", 
            (int.from_bytes(whole[4:6], "little"))), flush = True)
        context.present(console)  # Show the console.

while True:
    # This event loop will wait until at least one event is processed before exiting.
    # For a non-blocking event loop replace `tcod.event.wait` with `tcod.event.get`.
    for event in tcod.event.wait():
        context.convert_event(event)  # Sets tile coordinates for mouse events.
        if isinstance(event, tcod.event.Quit):
            raise SystemExit()