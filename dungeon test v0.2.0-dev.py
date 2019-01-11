"""-------------------------------------------------------------------------#
# "Dungeon Test"                                                             #
# By Douglas J. Honeycutt                                                   #
# https://withacact.us/ | https://github.com/RidleyofZebes/hero-simulator   #
#-------------------------------------------------------------------------"""


# Imports...
import os
# import sys
import pickle  # <-- The thing that lets the save/load function work. Favorite module name.
import re  # <-- RegEx stuffs module
import pygame
import math
# from res import pygame_textinput
# from random import randint  # <-- LulZ S000 RaNdUm
# from natural.number import ordinal  # <-- Makes the numbers look pretty - 1st, 2nd, 3rd, 4th...

pygame.init()
title = "dungeon test v0.2.0-dev"

window_res = (1280, 720)
FPS = 30

gw = pygame.display.set_mode(window_res)
pygame.display.set_caption(title)

pygame.key.set_repeat(10, 50)

clock = pygame.time.Clock()

# Colors
black = (0, 0, 0)
dkgray = (32, 32, 32)
ltgray = (169, 169, 169)
white = (255, 255, 255)
red = (255, 0, 0)
orange = (255, 128, 0)
green = (0, 255, 0)
dkgreen = (1, 50, 32)
blue = (0, 0, 255)
purple = (78, 48, 132)

# Font(s)
font = pygame.font.Font('res/alkhemikal.ttf', 28)

# Image(s)
frame = pygame.image.load('res/window_wide.png')
heroico = pygame.image.load('res/maphero.png')


# Test starts here
class Map:
    def __init__(self):
        self.defaultxy = (486, 247)
        self.height = 100
        self.width = 100
        self.offsetX = 129
        self.offsetY = 643
        self.tile_size = 25
        self.tile_margin = 1
        self.grid = {}


class Player:
    def __init__(self):
        self.name = "Nameless"
        self.x = 0
        self.y = 0
        self.viewrange = 5
        self.icon = heroico
        self.rotation = 0

        # self.killcount = 0
        # self.encounter = 0
        # self.gametime = 0
        # self.xp = 0
        # self.lvl = 1
        # self.gold = 0

    def move(self, direction):
        if self.rotation == 0:
            facing = "N"
        if self.rotation == 180:
            facing = "S"
        if self.rotation == -90:
            facing = "E"
        if self.rotation == 90:
            facing = "W"
        if direction == "forward":
            if facing == "N":
                if self.x == 0:
                    print("Out of Range")
                elif map.grid[self.x - 1][self.y]["isWall"] == 1:
                    print("Blocked")
                else:
                    self.x -= 1
                    map.offsetX += (map.tile_size + map.tile_margin)
            if facing == "S":
                if self.x == map.height - 1:
                    print("Out of Range")
                elif map.grid[self.x + 1][self.y]["isWall"] == 1:
                    print("Blocked")
                else:
                    self.x += 1
                    map.offsetX -= (map.tile_size + map.tile_margin)
            if facing == "W":
                if self.y == 0:
                    print("Out of Range")
                elif map.grid[self.x][self.y - 1]["isWall"] == 1:
                    print("Blocked")
                else:
                    self.y -= 1
                    map.offsetY += (map.tile_size + map.tile_margin)
            if facing == "E":
                if self.y == map.width - 1:
                    print("Out of Range")
                elif map.grid[self.x][self.y + 1]["isWall"] == 1:
                    print("Blocked")
                else:
                    self.y += 1
                    map.offsetY -= (map.tile_size + map.tile_margin)
        if direction == "backward":
            if facing == "S":
                if self.x == 0:
                    print("Out of Range")
                elif map.grid[self.x - 1][self.y]["isWall"] == 1:
                    print("Blocked")
                else:
                    self.x -= 1
                    map.offsetX += (map.tile_size + map.tile_margin)
            if facing == "N":
                if self.x == map.height - 1:
                    print("Out of Range")
                elif map.grid[self.x + 1][self.y]["isWall"] == 1:
                    print("Blocked")
                else:
                    self.x += 1
                    map.offsetX -= (map.tile_size + map.tile_margin)
            if facing == "E":
                if self.y == 0:
                    print("Out of Range")
                elif map.grid[self.x][self.y - 1]["isWall"] == 1:
                    print("Blocked")
                else:
                    self.y -= 1
                    map.offsetY += (map.tile_size + map.tile_margin)
            if facing == "W":
                if self.y == map.width - 1:
                    print("Out of Range")
                elif map.grid[self.x][self.y + 1]["isWall"] == 1:
                    print("Blocked")
                else:
                    self.y += 1
                    map.offsetY -= (map.tile_size + map.tile_margin)

    def strafe(self, direction):
        if self.rotation == 0:
            facing = "N"
        if self.rotation == 180:
            facing = "S"
        if self.rotation == -90:
            facing = "E"
        if self.rotation == 90:
            facing = "W"
        if facing == "N":
            if direction == "left":
                if self.y == 0:
                    print("Out of Range")
                elif map.grid[self.x][self.y - 1]["isWall"] == 1:
                    print("Blocked")
                else:
                    self.y -= 1
                    map.offsetY += (map.tile_size + map.tile_margin)
            if direction == "right":
                if self.y == map.width - 1:
                    print("Out of Range")
                elif map.grid[self.x][self.y + 1]["isWall"] == 1:
                    print("Blocked")
                else:
                    self.y += 1
                    map.offsetY -= (map.tile_size + map.tile_margin)
        if facing == "S":
            if direction == "right":
                if self.y == 0:
                    print("Out of Range")
                elif map.grid[self.x][self.y - 1]["isWall"] == 1:
                    print("Blocked")
                else:
                    self.y -= 1
                    map.offsetY += (map.tile_size + map.tile_margin)
            if direction == "left":
                if self.y == map.width - 1:
                    print("Out of Range")
                elif map.grid[self.x][self.y + 1]["isWall"] == 1:
                    print("Blocked")
                else:
                    self.y += 1
                    map.offsetY -= (map.tile_size + map.tile_margin)
        if facing == "E":
            if direction == "left":
                if self.x == 0:
                    print("Out of Range")
                elif map.grid[self.x - 1][self.y]["isWall"] == 1:
                    print("Blocked")
                else:
                    self.x -= 1
                    map.offsetX += (map.tile_size + map.tile_margin)
            if direction == "right":
                if self.x == map.height - 1:
                    print("Out of Range")
                elif map.grid[self.x + 1][self.y]["isWall"] == 1:
                    print("Blocked")
                else:
                    self.x += 1
                    map.offsetX -= (map.tile_size + map.tile_margin)
        if facing == "W":
            if direction == "left":
                if self.x == map.height - 1:
                    print("Out of Range")
                elif map.grid[self.x + 1][self.y]["isWall"] == 1:
                    print("Blocked")
                else:
                    self.x += 1
                    map.offsetX -= (map.tile_size + map.tile_margin)
            if direction == "right":
                if self.x == 0:
                    print("Out of Range")
                elif map.grid[self.x - 1][self.y]["isWall"] == 1:
                    print("Blocked")
                else:
                    self.x -= 1
                    map.offsetX += (map.tile_size + map.tile_margin)

    def rotate(self, turn):
        cardinal = (0, -90, 180, 90)  # (0 = N), (90 = W), (180 = S), (-90 = E)
        for x in range(len(cardinal)):
            if self.rotation == cardinal[x]:
                x += turn
                if x >= len(cardinal):
                    x -= len(cardinal)
                self.rotation = cardinal[x]
                print("Rotated to " + str(cardinal[x]) + " degrees")
                return


def message(text, *texloc, color=white):
    defaultcolor = color
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = 500, 255
    if not texloc:
        pos = 20, 330
    else:
        pos = texloc
    x, y = pos
    for line in words:
        for word in line:
            color = defaultcolor
            if re.search('<!(.*):>',
                         word):  # Searches for text wrapped in <!these characters:>, which is used here to change the color of the word.
                colorcheck = re.search('<!(.*):>', word)  # Assigns the captured string to a variable.
                strip = re.sub(r'\W', "",
                               colorcheck.group())  # Removes everything from the string except the word, in this case, the color.
                word = re.sub(colorcheck.group(), "", word)  # Removes the flag and keyword from the text for cleanup.
                word_surface = font.render(word, False,
                                           color)  # Re-renders and gets the new size of the word after the flag has been removed.
                word_width, word_height = word_surface.get_size()
                color = eval(strip)
                if x + word_width >= max_width:
                    x = pos[0]
                    y += word_height
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            gw.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.


def save():
    print("Saving...")
    data = {'dungeon': map.grid,
            'player': (player.x, player.y, player.rotation),
            'offset': (map.offsetX, map.offsetY),
            'viewport': (map.tile_size, map.tile_margin)
            }
    with open('save/dungeon3.sav', 'wb') as f:
        pickle.dump(data, f)
    print("Dungeon Saved")


def load():
    print("Loading...")
    with open('save/dungeon3.sav', 'rb') as f:
        data = pickle.load(f)
    map.grid = data['dungeon']
    player.x, player.y, player.rotation = data['player']
    map.offsetX, map.offsetY = data['offset']
    map.tile_size, map.tile_margin = data['viewport']
    print("Dungeon Loaded")


def reset_map():
    # print("Map Reset Disabled, use Map Editor.")
    print("Resetting Map...")
    player.x = 0
    player.y = 0
    map.offsetX = map.defaultxy[1]
    map.offsetY = map.defaultxy[0]
    # map.grid = [[1 for x in range(map.width)] for y in range(map.height)]
    map.grid = [
        [{"ID": 1,
          "name": "Stone Floor",
          "color": (169, 169, 169),
          "isVisible": 0,
          "isDiscovered": 0,
          "isWall": 0}
         for x in range(map.width)]
         for y in range(map.height)]
    print("Map reset")

map = Map()
player = Player()

load()


def main():
    RAYS = 360  # Should be 360!

    STEP = 3  # The step of for cycle. More = Faster, but large steps may
    # cause artifacts. Step 3 is great for radius 10.

    # Tables of precalculated values of sin(x / (180 / pi)) and cos(x / (180 / pi))
    sintable = []
    costable = []

    for x in range (0, 361):
        sincalc = math.sin(x/(180/math.pi))
        sintable.append(sincalc)
        coscalc = math.cos(x/(180/math.pi))
        costable.append(coscalc)


    mapdisplay = 0  # Needs to be in some sort of window state class...
    tile_desc = ""  # Also an environment variable... better put it in the class, too.

    running = True
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            # Grid Click Events #####
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if pos[0] > 529 and pos[1] > 14 and pos[0] < 785 and pos[
                    1] < 270:  # Only take action for clicks within the minimap
                    column = (pos[0] - map.offsetY) // (map.tile_size + map.tile_margin)
                    row = (pos[1] - map.offsetX) // (map.tile_size + map.tile_margin)
                    print("Left Click ", pos, "Grid coordinates: ", row, column)
                    if row < 0 or column < 0 or row > map.width - 1 or column > map.height - 1:
                        print("Invalid")
                    elif row == player.x and column == player.y:
                        print("Player")
                    elif map.grid[row][column] == 1:
                        map.grid[row][column] = 2
                        print("Selected")
                    elif map.grid[row][column] == 2:
                        map.grid[row][column] = 1
                        print("Deselected")
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                pos = pygame.mouse.get_pos()
                if pos[0] > 529 and pos[1] > 14 and pos[0] < 785 and pos[
                    1] < 270:  # Only take action for clicks within the minimap
                    column = (pos[0] - map.offsetY) // (map.tile_size + map.tile_margin)
                    row = (pos[1] - map.offsetX) // (map.tile_size + map.tile_margin)
                    print("Right Click ", pos, "Grid coordinates: ", row, column)
                    if row == player.x and column == player.y:
                        tile_desc = "Player"
                        print(tile_desc)
                    else:
                        tile_desc = map.grid[row][column]["name"]
                        print(tile_desc)

            # Player Movement #####
            if event.type == pygame.KEYDOWN:
                multikey = pygame.key.get_pressed()
                if event.key == pygame.K_w:
                    print("Move Forward")
                    player.move("forward")
                    print("Moved to", player.x, player.y)
                if event.key == pygame.K_s:
                    print("Move Back")
                    player.move("backward")
                    print("Moved to", player.x, player.y)
                if multikey[pygame.K_LSHIFT] and multikey[pygame.K_a]:
                    print("Strafe Left")
                    player.strafe("left")
                    print("Moved to", player.x, player.y)
                elif event.key == pygame.K_a:
                    print("Turn Right")
                    player.rotate(-1)
                if multikey[pygame.K_LSHIFT] and multikey[pygame.K_d]:
                    print("Strafe Right")
                    player.strafe("right")
                    print("Moved to", player.x, player.y)
                elif event.key == pygame.K_d:
                    print("Turn Left")
                    player.rotate(1)
                if event.key == pygame.K_e:
                    print("Examine/Interact not yet implemented, but reserved.")
                if event.key == pygame.K_ESCAPE:
                    print("Shutting down...")
                    running = False

                # Multikey Commands #####
                if multikey[pygame.K_LCTRL] and multikey[pygame.K_z]:
                    save()
                if multikey[pygame.K_LCTRL] and multikey[pygame.K_x]:
                    load()
                if multikey[pygame.K_LCTRL] and multikey[pygame.K_r]:
                    reset_map()

                if multikey[pygame.K_LCTRL] and multikey[pygame.K_m]:
                    print("Switching Maps...")
                    if mapdisplay == 0:
                        mapdisplay = 1
                    elif mapdisplay == 1:
                        mapdisplay = 0
                    print("Switched to Display " + str(mapdisplay))

        """ Begin drawing the game screen """

        gw.fill(dkgray)

        if mapdisplay == 0:

            # Create the 4 main surfaces: viewscreen, minimap, textbox, and menu

            viewscreen = pygame.Surface((999, 527))
            minimap = pygame.Surface((256, 256))
            textbox = pygame.Surface((999, 168))
            statmenu = pygame.Surface((257, 439))

            """ Draw the map """

            # Reset visible squares...
            for x in range(map.height):
                for y in range(map.width):
                    if map.grid[x][y]["isVisible"] == 1:
                        map.grid[x][y]["isVisible"] = 0

            # Determine which squares are visible...
            for i in range(0, RAYS + 1, STEP):
                ax = sintable[i]  # Get precalculated value sin(x / (180 / pi))
                ay = costable[i]  # cos(x / (180 / pi))
                x = player.x  # Player's x
                y = player.y  # Player's y
                for z in range(player.viewrange):  # Cast the ray
                    x += ax
                    y += ay
                    if x < 0 or y < 0 or x > map.width or y > map.height:  # If ray is out of range
                        break
                    map.grid[int(round(x))][int(round(y))].update({"isDiscovered": 1, "isVisible": 1})  # Discover the tile and make it visible
                    if map.grid[int(round(x))][int(round(y))]["isWall"] == 1:  # Stop ray if it hit
                        break

            map.grid[player.x][player.y].update({"isDiscovered": 1, "isVisible": 1})

            for x in range(map.height):
                for y in range(map.width):
                    tile = pygame.Surface((map.tile_size, map.tile_size))
                    tile.fill((map.grid[x][y].get("color")))
                    if map.grid[x][y].get("isVisible") == 0 and map.grid[x][y].get(
                            "isDiscovered") == 1:  # Not useful for Map Editor, but VERY YES in Game Engine.
                        tile.set_alpha(64)
                    if map.grid[x][y].get("isVisible") == 0 and map.grid[x][y].get("isDiscovered") == 0:
                        tile.fill(black)
                    viewscreen.blit(tile, ((map.tile_margin + map.tile_size) * y + map.tile_margin + map.offsetY,
                                           (map.tile_margin + map.tile_size) * x + map.tile_margin + map.offsetX))
                    # if x == player.x and y == player.y:
                    #     playerico = pygame.transform.rotate(player.icon, player.rotation)
                    #     playerico = pygame.transform.scale(playerico, (map.tile_size, map.tile_size))
                    #     viewscreen.blit(playerico, ((player.y * (map.tile_size + map.tile_margin)) + map.offsetY + 1,
                    #                                 (player.x * (map.tile_size + map.tile_margin)) + map.offsetX + 1))

            """ Draw the Player Icon """
            maparrow = pygame.transform.rotate(player.icon, player.rotation)
            viewscreen.blit(maparrow, ((player.y * (map.tile_size + map.tile_margin)) + map.offsetY + 1,
                                       (player.x * (map.tile_size + map.tile_margin)) + map.offsetX + 1))

            """ Tile Descriptions? """
            tiledescrect = font.render(tile_desc, False, black)
            descrect = tiledescrect.get_rect()
            descrect.center = (658, 300)
            # gw.blit(tiledescrect, descrect)

            # message("Welcome, <!red:>Hero! Your destiny awaits.")

            # Create the 4 main surfaces: viewscreen, minimap, textbox, and menu

            gw.blit(viewscreen, (10, 10))
            gw.blit(minimap, (1014, 10))
            gw.blit(textbox, (10, 542))
            gw.blit(statmenu, (1014, 271))




        if mapdisplay == 1:  # Supposed to be the map screen. Needs massive alterations.
            for x in range(map.height):
                for y in range(map.width):
                    if map.grid[x][y]["isVisible"] == 0:
                        color = black
                    elif map.grid[x][y]["floor"] == 1:
                        color = ltgray
                    elif map.grid[x][y]["isWall"] == 1:
                        color = green
                    if map.grid[x][y]["isVisible"] == 0 and map.grid[x][y]["isDiscovered"] == 1:
                        if map.grid[x][y]["floor"] == 1:
                            color = dkgray
                        elif map.grid[x][y]["isWall"] == 1:
                            color = dkgreen
                    if x == player.x and y == player.y:
                        color = red
                    pygame.draw.rect(gw, color, ((1 + 5) * y + 1, (1 + 5) * x + 1, 5, 5),
                                     0)  # Needs work, supposed to display map scalable and scrollable. For now just barely managable (somehow).

        clock.tick(FPS)

        pygame.display.update()

if __name__ == '__main__':
    main()

pygame.display.quit()
pygame.quit()
print("Goodbye, thanks for playing!")
os._exit(1)