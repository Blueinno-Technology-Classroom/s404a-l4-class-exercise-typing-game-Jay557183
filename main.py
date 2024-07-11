import pgzrun
from pgzhelper import *
WIDTH = 1000
HEIGHT = 800
zombie_run_img = ["zombie/run/tile002", "zombie/run/tile003", "zombie/run/tile004", "zombie/run/tile005"]
player_idle_img = ["player/idle/tile000","player/idle/tile001","player/idle/tile002","player/idle/tile003","player/idle/tile004","player/idle/tile005"]
player_die_img = ["player/die/tile000","player/die/tile001","player/die/tile002","player/die/tile003","player/die/tile004","player/die/tile005","player/die/tile006"]
zombie = Actor(zombie_run_img[0])
zombie.images = zombie_run_img
zombie.scale = 5
zombie.fps = 10
zombie.right = WIDTH
zombie.bottom = HEIGHT
player = Actor(player_idle_img[0])
player.images = player_idle_img
player.fps = 20
player.scale = 3
player.bottom = HEIGHT + 200
question = "hello world"
response = ""
def update():
    global response
    zombie.animate()
    player.animate()
    zombie.x -= 1
    if not(player.image in player_die_img):
        zombie.x -= 1
    if player.image == player_die_img[-1]:
        player.images = player_idle_img
    if zombie.left <= 0:
        zombie.right = WIDTH + 100
        response = " "
    if zombie.collide_pixel(player):
        zombie.right = WIDTH + 100
        response = " "
        player.images = player_die_img
        player.fps = 10
def on_key_down(key):
    global response
    if key in range(97, 123):
        print(chr(key))
        response += chr(key)
    elif key == keys.SPACE:
        response += " "
    elif key == keys.BACKSPACE:
        response = response[0:-1]
def draw():
    screen.clear()
    screen.draw.text(question, (150, 100), fontsize=75)
    screen.draw.text(response, (150, 100), fontsize=75, color="blue")
    zombie.draw()
    player.draw()
pgzrun.go()