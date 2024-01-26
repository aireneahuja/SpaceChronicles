# Space Chronicles by Airene Ahuja

'''A single player game that follows the following storyline:
The character is stuck on their damaged spaceship, and they
must remove the debris and collect the cogs to do repairs
so they can fight off the aliens again.

The player starts on a single screen where they use the arrow
keys to move around and accomplish the task described. Once
done, the screen switches to a shooter game.

In this portion, the player moves side to side and shoots at
the enemies that descend from the top. If one of them gets
past, it reduces the player's health.

Upon the player's inevitable death, they are told that their
spaceship is damaged again, and the game repeats from there
in what is essentially a never ending loop.
'''

import simplegui, math, random

# Stages
START_SCREEN = 0
STAGE1 = 1
STAGE2 = 2
GAMEOVER = 3

# Frame constants
FRAME_HEIGHT = 600
FRAME_WIDTH = 800
FRAME_CENTER = [800 / 2, 600 / 2]

# Start screen constants
STARTSCREEN_IMG = simplegui.load_image(
    "https://c4.wallpaperflare.com/wallpaper/542/247/774/digital-art-space-stars-black-earth-hd-wallpaper-preview.jpg")
STARTSCREEN_SIZE = [546, 410]
STARTSCREEN_CENTER = [728 / 2, 410 / 2]

# Title and text constants
TITLE_SIZE = 85
TITLE_POS = [25, 100]

LINE1_POS = [550, 200]
LINE2_POS = [550, 225]
LINE3_POS = [550, 250]
LINE4_POS = [550, 275]
LINE5_POS = [550, 300]
LINE6_POS = [550, 325]
LINE7_POS = [550, 350]
LINE8_POS = [550, 375]

TEXT_COLOUR = "white"
TEXT_SIZE = 15
FONT = "monospace"

# Images on start screen
ASTRONAUT_SIZE = [120, 120]
ASTRONAUT_ROTATION = -0.4
ASTRONAUT_POS = [425, 515]

SHIP_SIZE = [250, 229]
SHIP_ROTATION = 0.6
SHIP_POS = [150, 280]

TETHER_IMG = simplegui.load_image("https://i.imgur.com/BqkFgKk.png")
TETHER_IMGCENTER = [1280 / 2, 1280 / 2]
TETHER_IMGSIZE = [1280, 1280]
TETHER_CENTER = [200, 405]
TETHER_SIZE = [500, 375]

# Play button constants
PLAY_IMG = simplegui.load_image("https://i.imgur.com/HUxPwpD.png")
PLAY_IMGWIDTH = 299
PLAY_IMGHEIGHT = 170
PLAY_WIDTH = 200
PLAY_HEIGHT = 114
PLAY_POS = [650, 500]

# Background stage one constants
BACKGROUND_IMG = simplegui.load_image("https://i.imgur.com/DU4rFu6.jpg")
BCGD_IMGSIZE = [644, 464]
BCGD_CENTER = [644 / 2, 464 / 2]

# Player - stage one
PLAYER_IMG = simplegui.load_image("https://easydrawingguides.com/wp-content/uploads/2018/10/Astronaut-10.png")
PLAYER_IMGSIZE = [680, 678]
PLAYER_CENTER = [680 / 2, 678 / 2]
PLAYER_SIZE = [100, 100]
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 100
player_speed_x = 3
player_speed_y = 3
PLAYER_ROTATION = 0

# Cogs variables and constants
COG_IMG = simplegui.load_image(
    "https://pixelartmaker-data-78746291193.nyc3.digitaloceanspaces.com/image/b1c49e7f345d87d.png")
COG_IMGSIZE = [300, 300]
COG_CENTER = [300 / 2, 300 / 2]
COG_SIZE = [20, 20]
COG_WIDTH = 20
cogspawn_interval = 60
cog_points = 1
cogs = []
final_cog_score = 50
cog_score = 0

# Rocks/debris variables and constants
DEBRIS_IMG = simplegui.load_image(
    "https://toppng.com/public/uploads/thumbnail/dirt-debris-png-rock-debris-11563018511sbwwyar8oh.png")
DEBRIS_IMGSIZE = [280, 272]
DEBRIS_CENTER = [280 / 2, 272 / 2]
DEBRIS_SIZE = [30, 30]
DEBRIS_WIDTH = 30
DEBRIS_HEIGHT = 30
debris_amount = 25
debris = []

# Constants for labels throughout game play
LABEL_SIZE = 25
LABEL_COLOUR = "#43F0F8"
COG_LABEL_POS = [10, 60]
DEBRIS_LABEL_POS = [10, 30]
HEALTH_LABEL_POS = [15, 40]
POINTS_LABEL_SIZE = 35

# Weapon variable and consants
WEAPON_IMG = simplegui.load_image(
    "https://www.pinclipart.com/picdir/big/567-5671634_bullet-drawing-scar-pixelated-gun-png-clipart.png")
WEAPON_IMGSIZE = [1117, 451]
WEAPON_CENTER = [1117 / 2, 451 / 2]
WEAPON_SIZE = [50, 20]
WEAPON_WIDTH = 50
WEAPON_HEIGHT = 20
weapon_position = [random.randrange(FRAME_WIDTH),
                   random.randrange(FRAME_HEIGHT)]
draw_weapon = True

# Continue button variable and constants
CONTINUE_IMG = simplegui.load_image("https://i.imgur.com/F0HFpk0.png")
CONT_IMG_WIDTH = 679
CONT_IMG_HEIGHT = 122
CONTINUE_WIDTH = 425
CONTINUE_HEIGHT = 76
draw_cont_button = False

# Text that accompanies continue button
CONT_TEXT_SIZE = 18
CONT_TEXT_POS1 = [55, 470]
CONT_TEXT_POS2 = [45, 500]
CONT_TEXT_POS3 = [45, 530]

# Background stage two
NEW_BACKGROUND = simplegui.load_image("https://i.imgur.com/ESyF0nT.jpg")
NEW_BCGD_SIZE = [510, 339]
NEW_BCGD_CENTER = [510 / 2, 339 / 2]

# Player stage two
SPACESHIP_IMG = simplegui.load_image(
    "https://www.nicepng.com/png/full/13-138961_vector-spaces-ship-8-bit-spaceship-sprite.png")
SPACESHIP_IMGSIZE = [577, 529]
SPACESHIP_CENTER = [577 / 2, 529 / 2]
SPACESHIP_SIZE = [117, 106]
SPACESHIP_WIDTH = 117
SPACESHIP_HEIGHT = 106
SPACESHIP_POS = [FRAME_WIDTH / 2, FRAME_HEIGHT - SPACESHIP_HEIGHT / 2]
player_health = 100

# The boundary at which the player's health decreases
BOUNDARY = FRAME_HEIGHT - SPACESHIP_WIDTH

# Bullets
BULLET_IMG = simplegui.load_image("https://i.imgur.com/vcEMyLg.png")
BULLET_IMGSIZE = [373, 573]
BULLET_CENTER = [373 / 2, 573 / 2]
BULLET_SIZE = [6, 9]
BULLET_WIDTH = 6
BULLET_HEIGHT = 9
bullet_attack = 1
bullet_speed = -4
bullets = []
bullets_shot = 0

# Enemy variables
enemies = []
enemies_points = 0
start_spawn_enemy = False
enemies_killed = 0
enemies_passed = 0
high_score = enemies_points

# First enemy
ENEMY1_IMG = simplegui.load_image("https://i.imgur.com/OeVpUPD.png")
ENEMY1_IMG_SIZE = [310, 310]
ENEMY1_IMG_WIDTH = 310
ENEMY1_CENTER = [310 / 2, 310 / 2]
ENEMY1_SIZE = [75, 75]
ENEMY1_WIDTH = 75
ENEMY1_HEIGHT = 75
ENEMY1_SPEED = [0, 3]
ENEMY1_ATTACK = 5
enemy1_health = 1

# Second enemy
ENEMY2_IMG = simplegui.load_image("https://i.imgur.com/VNzhquw.png")
ENEMY2_IMG_WIDTH = 1280
ENEMY2_CENTER = [1280 / 2, 1280 / 2]
ENEMY2_SIZE = [99, 99]
ENEMY2_WIDTH = 99
ENEMY2_HEIGHT = 99
ENEMY2_SPEED = [0, 3]
ENEMY2_ATTACK = 7
enemy2_health = 2

# Third enemy
ENEMY3_IMG = simplegui.load_image("https://opengameart.org/sites/default/files/ship_011.png")
ENEMY3_IMG_WIDTH = 512
ENEMY3_CENTER = [512 / 2, 512 / 2]
ENEMY3_SIZE = [117, 117]
ENEMY3_WIDTH = 117
ENEMY3_HEIGHT = 117
ENEMY3_SPEED = [0, 3]
ENEMY3_ATTACK = 10
enemy3_health = 3

# Amount of time between enemy spawns in milliseconds
time_interval = 2000

# Game-over background
GAMEOVER_IMG = simplegui.load_image("https://i.imgur.com/pqPIeUu.png")
GAMEOVER_SIZE = [250, 191]
GAMEOVER_CENTER = [250 / 2, 191 / 2]

# Gameover message position
GAMEOVER_LINE1_POS = [50, 80]
GAMEOVER_LINE2_POS = [270, 120]

# Stats label positions
BULLETS_SHOT_POS = [30, 440]
ENEMIES_KILLED_POS = [30, 485]
ENEMIES_PASSED_POS = [30, 530]
ENEMIES_POINTS_POS = [320, 460]
HIGH_SCORE_POS = [315, 510]
STATS_SIZE = 22

# Replay button constants
REPLAY_IMG = simplegui.load_image("https://i.imgur.com/uyIxOoK.png")
REPLAY_IMGWIDTH = 419
REPLAY_IMGHEIGHT = 131
REPLAY_WIDTH = 210
REPLAY_HEIGHT = 65
REPLAY_POS = [655, 480]
draw_replay = False


# HELPER FUNCTIONS
def start_screen():
    global background
    global stage
    global spaceship
    global astronaut
    global play_button

    stage = START_SCREEN
    background = Background(STARTSCREEN_IMG, STARTSCREEN_CENTER,
                            STARTSCREEN_SIZE, )

    # Button and images on start screen
    spaceship = Character(SPACESHIP_IMG, SPACESHIP_IMGSIZE,
                          SHIP_POS, SPACESHIP_WIDTH,
                          SPACESHIP_HEIGHT, SPACESHIP_CENTER,
                          SHIP_SIZE, SHIP_ROTATION)

    astronaut = Character(PLAYER_IMG, PLAYER_IMGSIZE,
                          ASTRONAUT_POS, PLAYER_WIDTH,
                          PLAYER_HEIGHT, PLAYER_CENTER,
                          ASTRONAUT_SIZE, ASTRONAUT_ROTATION)

    play_button = Button(PLAY_IMG, PLAY_IMGWIDTH, PLAY_IMGHEIGHT,
                         PLAY_POS, PLAY_WIDTH, PLAY_HEIGHT)


# New game function - shows up when the game loads
def new_game():
    global stage
    global player
    global background

    stage = STAGE1
    background = Background(BACKGROUND_IMG, BCGD_CENTER, BCGD_IMGSIZE)
    player = Character(PLAYER_IMG, PLAYER_IMGSIZE,
                       FRAME_CENTER.copy(), PLAYER_WIDTH,
                       PLAYER_HEIGHT, PLAYER_CENTER,
                       PLAYER_SIZE, PLAYER_ROTATION)
    # Creates debris
    for i in range(debris_amount):
        new_debris()


# General Distance Calculator using pythagoras
def distance(pos1, pos2):
    # Uses Pythagoras to calculate distance
    a = pos1[0] - pos2[0]
    b = pos1[1] - pos2[1]
    c = math.sqrt(a ** 2 + b ** 2)
    return c


# Horizontal Distance Calculator
def distance_x(pos1, pos2):
    # Checking which value is greater
    # so the distance is a positive number
    if pos2[0] >= pos1[0]:
        c = pos2[0] - pos1[0]
    if pos1[0] > pos2[0]:
        c = pos1[0] - pos2[0]
    return c


# Vertical Distance Calculator
def distance_y(pos1, pos2):
    # Checking which value is greater
    # so the distance is a positive number
    if pos2[1] >= pos1[1]:
        c = pos2[1] - pos1[1]
    if pos1[1] > pos2[1]:
        c = pos1[1] - pos2[1]
    return c


# Function to spawn cogs
def spawn_cog():
    position = [random.randrange(FRAME_WIDTH),
                random.randrange(FRAME_HEIGHT)]

    new_cog = Cog(COG_IMG, position)
    cogs.append(new_cog)


# Function to create debris
def new_debris():
    position = [random.randrange(FRAME_WIDTH),
                random.randrange(FRAME_HEIGHT)]
    rock = Debris(DEBRIS_IMG, position)
    debris.append(rock)


# Function to spawn the weapon
def spawn_weapon():
    global weapon

    weapon = Weapon(WEAPON_IMG, weapon_position)


# Function to draw the "continue" button
def draw_continue_button():
    global cont_button
    global draw_weapon

    cont_button = Button(CONTINUE_IMG, CONT_IMG_WIDTH,
                         CONT_IMG_HEIGHT, FRAME_CENTER.copy(),
                         CONTINUE_WIDTH, CONTINUE_HEIGHT)
    draw_weapon = False


# Switch to stage two
def switch_handler():
    global stage
    global background
    global draw_cont_button
    global player
    global player_speed_y
    global player_speed_x
    global start_spawn_enemy

    stage = STAGE2
    draw_cont_button = False
    background = Background(NEW_BACKGROUND, NEW_BCGD_CENTER, NEW_BCGD_SIZE)
    player = Character(SPACESHIP_IMG, SPACESHIP_IMGSIZE,
                       SPACESHIP_POS.copy(), SPACESHIP_WIDTH,
                       SPACESHIP_HEIGHT, SPACESHIP_CENTER,
                       SPACESHIP_SIZE, PLAYER_ROTATION)
    player_speed_y = 0
    player_speed_x = 3.5
    start_spawn_enemy = True


# Function to shoot bullet
def shoot_bullet():
    global bullets_shot

    if stage == STAGE2:
        position = [player.pos[0], BOUNDARY]
        new_bullet = Bullet(BULLET_IMG, position)
        bullets.append(new_bullet)
        bullets_shot += 1


# Function to spawn the enemies
def spawn_enemy():
    global enemies
    if stage == STAGE2:
        if start_spawn_enemy:

            # Sets position of the next enemy, with the vertical
            # position compensating for the height of the enemy
            position = [random.randrange(FRAME_WIDTH),
                        0 - ENEMY1_WIDTH]

            if enemies_killed + 1 <= 10:
                new_enemy = Enemy(ENEMY1_IMG, ENEMY1_IMG_WIDTH,
                                  position, ENEMY1_WIDTH, ENEMY1_HEIGHT,
                                  ENEMY1_SPEED, ENEMY1_ATTACK, enemy1_health)

            if enemies_killed + 1 > 10 and enemies_killed + 1 <= 20:
                new_enemy = Enemy(ENEMY2_IMG, ENEMY2_IMG_WIDTH,
                                  position, ENEMY2_WIDTH, ENEMY2_HEIGHT,
                                  ENEMY2_SPEED, ENEMY2_ATTACK, enemy2_health)

            if enemies_killed + 1 > 20:
                new_enemy = Enemy(ENEMY3_IMG, ENEMY3_IMG_WIDTH,
                                  position, ENEMY3_WIDTH, ENEMY3_HEIGHT,
                                  ENEMY3_SPEED, ENEMY3_ATTACK, enemy3_health)

            enemies.append(new_enemy)


# Game over handler
def game_over():
    global stage
    global background
    global draw_replay
    global start_spawn_enemy
    stage = GAMEOVER
    background = Background(GAMEOVER_IMG, GAMEOVER_CENTER, GAMEOVER_SIZE)
    draw_replay = True
    enemy_timer.stop()
    start_spawn_enemy = False


# Function to draw the replay button
def draw_replay_button():
    global replay_button
    replay_button = Button(REPLAY_IMG, REPLAY_IMGWIDTH,
                           REPLAY_IMGHEIGHT, REPLAY_POS,
                           REPLAY_WIDTH, REPLAY_HEIGHT)


# Replay handler
def replay():
    global player_speed_x
    global player_speed_y
    global debris_amount
    global cogspawn_interval
    global cogs
    global cog_score
    global final_cog_score
    global draw_weapon
    global player_health
    global bullets
    global bullets_shot
    global start_spawn_enemy
    global enemies
    global enemies_killed
    global enemies_passed
    global enemies_points

    # Resets variables to the values they had at beginning
    player_speed_x = 3
    player_speed_y = 3
    debris_amount = 20
    cogspawn_interval = 60
    cogs = []
    cog_score = 0
    final_cog_score = 40
    draw_weapon = True
    player_health = 100
    bullets = []
    bullets_shot = 0
    start_spawn_enemy = False
    enemies = []
    enemies_killed = 0
    enemies_passed = 0
    enemies_points = 0

    # Calls the new game function
    new_game()


# CLASSES

class Background:
    def __init__(self, image, center, image_size):
        self.img = image
        self.center = center
        self.img_size = image_size

    def draw(self, canvas):
        canvas.draw_image(self.img,
                          self.center,
                          self.img_size,
                          FRAME_CENTER,
                          [FRAME_WIDTH, FRAME_HEIGHT])


class Character:

    def __init__(self, image, image_size, position, width, height, center, size, rotation):
        self.img = image
        self.pos = position
        self.vel = [0, 0]
        self.width = width
        self.height = height
        self.center = center
        self.image_size = image_size
        self.size = size
        self.health = player_health
        self.rotation = rotation

    def draw(self, canvas):
        canvas.draw_image(self.img,
                          self.center,
                          self.image_size,
                          self.pos,
                          self.size,
                          self.rotation)

        self.left = self.pos[0] - self.width / 2 + 5
        self.right = self.pos[0] + self.width / 2 - 5
        self.top = self.pos[1] - self.height / 2 + 7
        self.bottom = self.pos[1] + self.height / 2 - 5

    # Movement function (update position)
    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        if self.pos[0] >= FRAME_WIDTH or self.pos[0] <= 0:
            self.vel[0] = 0
        if self.pos[1] >= FRAME_HEIGHT or self.pos[1] <= 0:
            self.vel[1] = 0

    # General collision function
    def collide(self, other):
        dist = distance(self.pos, other.pos)
        if dist <= self.width / 2 + other.width / 2:
            return True

    # Horizontal collision function
    def collide_x(self, other):
        dist_x = distance_x(self.pos, other.pos)
        if other.pos[1] >= self.top and other.pos[1] <= self.bottom:
            if dist_x < self.width / 2 + other.width / 2:
                return True

    # Vertical collision function
    def collide_y(self, other):
        dist_y = distance_y(self.pos, other.pos)
        if other.pos[0] <= self.right and other.pos[0] >= self.left:
            if dist_y < self.height / 2 + other.height / 2:
                return True


class Cog:

    def __init__(self, image, position):
        self.img = image
        self.pos = position
        self.width = COG_WIDTH
        self.height = COG_WIDTH

    def draw(self, canvas):
        canvas.draw_image(COG_IMG,
                          COG_CENTER,
                          COG_IMGSIZE,
                          self.pos,
                          COG_SIZE)


class Debris:
    def __init__(self, image, position):
        self.img = image
        self.pos = position
        self.width = DEBRIS_WIDTH / 2
        self.height = DEBRIS_HEIGHT / 2

    def draw(self, canvas):
        canvas.draw_image(DEBRIS_IMG,
                          DEBRIS_CENTER,
                          DEBRIS_IMGSIZE,
                          self.pos,
                          DEBRIS_SIZE)

    # Movement function (update position)
    def update(self):
        if player.collide_x(self):
            self.pos[0] += player.vel[0]
        if player.collide_y(self):
            self.pos[1] += player.vel[1]


class Weapon:

    def __init__(self, image, position):
        self.img = image
        self.pos = position
        self.width = WEAPON_WIDTH
        self.height = WEAPON_HEIGHT / 2

    def draw(self, canvas):
        canvas.draw_image(WEAPON_IMG,
                          WEAPON_CENTER,
                          WEAPON_IMGSIZE,
                          self.pos,
                          WEAPON_SIZE)


class Button:

    def __init__(self, image, image_width, image_height,
                 position, width, height):
        self.img = image
        self.img_width = image_width
        self.img_height = image_height
        self.pos = position
        self.width = width
        self.height = height
        self.left = self.pos[0] - self.width / 2
        self.right = self.pos[0] + self.width / 2
        self.top = self.pos[1] - self.height / 2
        self.bottom = self.pos[1] + self.height / 2

    def draw(self, canvas):
        canvas.draw_image(self.img,
                          (self.img_width / 2, self.img_height / 2),
                          (self.img_width, self.img_height),
                          self.pos,
                          (self.width, self.height))

    # Button pressed function
    def is_selected(self, click_pos):
        if click_pos[0] >= self.left and click_pos[0] <= self.right:
            if click_pos[1] >= self.top and click_pos[1] <= self.bottom:
                return True
        return False


class Bullet:

    def __init__(self, image, position):
        self.img = image
        self.pos = position
        self.width = BULLET_WIDTH
        self.height = BULLET_HEIGHT

    def draw(self, canvas):
        canvas.draw_image(BULLET_IMG,
                          BULLET_CENTER,
                          BULLET_IMGSIZE,
                          self.pos,
                          BULLET_SIZE)


class Enemy:

    def __init__(self, image, image_width, position, width, height, velocity, attack, health):
        self.img = image
        self.img_width = image_width
        self.img_height = image_width
        self.pos = position
        self.width = width
        self.height = height
        self.vel = velocity
        self.attack = attack
        self.health = health
        self.points = attack

    def draw(self, canvas):
        canvas.draw_image(self.img,
                          (self.img_width / 2, self.img_height / 2),
                          (self.img_width, self.img_height),
                          self.pos,
                          (self.width, self.height))
        self.left = self.pos[0] - self.width / 2
        self.right = self.pos[0] + self.width / 2
        self.top = self.pos[1] - self.height / 2
        self.bottom = self.pos[1] + self.height / 2

        # Movement function (update position)

    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

    # Vertical collision
    def collide_y(self, other):
        dist_y = distance_y(self.pos, other.pos)
        if other.pos[0] <= self.right and other.pos[0] >= self.left:
            if dist_y < self.height / 4 + other.height / 2:
                return True

            # HANDLER FUNCTIONS


# Key press handler
def key_press(key):
    # Player only moves after Stage 1
    if stage > START_SCREEN:

        if key == simplegui.KEY_MAP['right'] or key == simplegui.KEY_MAP['d']:
            player.vel[0] = player_speed_x
        if key == simplegui.KEY_MAP['left'] or key == simplegui.KEY_MAP['a']:
            player.vel[0] = -player_speed_x
        if key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['w']:
            player.vel[1] = -player_speed_y
        if key == simplegui.KEY_MAP['down'] or key == simplegui.KEY_MAP['s']:
            player.vel[1] = player_speed_y
        if key == simplegui.KEY_MAP['space']:
            shoot_bullet()


# Key release handler
def key_release(key):
    # Player only moves after Stage 1
    if stage > START_SCREEN:
        if key == simplegui.KEY_MAP['right'] or key == simplegui.KEY_MAP['d']:
            player.vel[0] = 0
        if key == simplegui.KEY_MAP['left'] or key == simplegui.KEY_MAP['a']:
            player.vel[0] = 0
        if key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['w']:
            player.vel[1] = 0
        if key == simplegui.KEY_MAP['down'] or key == simplegui.KEY_MAP['s']:
            player.vel[1] = 0


# Mouse click handler
def mouse_click(mouse_position):
    if stage == START_SCREEN:
        if play_button.is_selected(mouse_position):
            new_game()

    if stage == STAGE1:
        if draw_cont_button:
            if cont_button.is_selected(mouse_position):
                switch_handler()

    if stage == GAMEOVER:
        if draw_replay:
            if replay_button.is_selected(mouse_position):
                replay()


# Main draw handler
def draw(canvas):
    global cog_score
    global debris_amount
    global cogspawn_interval
    global cogs
    global draw_cont_button
    global player_health
    global draw_replay
    global start_spawn_enemy
    global bullets_shot
    global enemies_killed
    global enemies
    global enemies_points
    global enemies_passed
    global high_score
    # Draw the background
    background.draw(canvas)

    # Stage 0 - Start screen
    if stage == START_SCREEN:
        # Draw images, text and button
        astronaut.draw(canvas)
        spaceship.draw(canvas)
        play_button.draw(canvas)

        canvas.draw_image(TETHER_IMG, TETHER_IMGCENTER,
                          TETHER_IMGSIZE, TETHER_CENTER,
                          TETHER_SIZE)
        canvas.draw_text("Space Chronicles", TITLE_POS,
                         TITLE_SIZE, TEXT_COLOUR, FONT)
        canvas.draw_text("The aliens have attacked your",
                         LINE1_POS, TEXT_SIZE, TEXT_COLOUR, FONT)
        canvas.draw_text("spaceship! Use the arrow keys",
                         LINE2_POS, TEXT_SIZE, TEXT_COLOUR, FONT)
        canvas.draw_text("or WASD to move around and",
                         LINE3_POS, TEXT_SIZE, TEXT_COLOUR, FONT)
        canvas.draw_text("push the debris off your ship",
                         LINE4_POS, TEXT_SIZE, TEXT_COLOUR, FONT)
        canvas.draw_text("while collecting cogs to do",
                         LINE5_POS, TEXT_SIZE, TEXT_COLOUR, FONT)
        canvas.draw_text("repairs. Then, once you get",
                         LINE6_POS, TEXT_SIZE, TEXT_COLOUR, FONT)
        canvas.draw_text("the weapon, fight off the",
                         LINE7_POS, TEXT_SIZE, TEXT_COLOUR, FONT)
        canvas.draw_text("aliens and save your planet!",
                         LINE8_POS, TEXT_SIZE, TEXT_COLOUR, FONT)

    # Stage 1 - Inside spaceship with cogs and rocks
    if stage == STAGE1:

        # Draw and update player
        player.draw(canvas)
        player.update()

        # Spawn cogs approximately once a second (random)
        if random.randrange(cogspawn_interval) == 1:
            spawn_cog()
        for cog in cogs:
            cog.draw(canvas)

            # Remove cog and increase score for each one
            if player.collide(cog):
                cogs.remove(cog)
                cog_score += cog_points

        # Cog amount label
        canvas.draw_text(str(cog_score) + "/" + str(final_cog_score) + " cogs",
                         COG_LABEL_POS, LABEL_SIZE,
                         LABEL_COLOUR, FONT)

        # Draws debris and moves it with the player
        for rock in debris:
            rock.draw(canvas)
            rock.update()

            # Removes rock when it reaches the edges
            if rock.pos[0] >= FRAME_WIDTH or rock.pos[0] <= 0:
                debris.remove(rock)
                debris_amount -= 1
                continue
            if rock.pos[1] >= FRAME_HEIGHT or rock.pos[1] <= 0:
                debris.remove(rock)
                debris_amount -= 1
                continue

        # Debris amount label
        canvas.draw_text(str(debris_amount) + " rocks left",
                         DEBRIS_LABEL_POS, LABEL_SIZE,
                         LABEL_COLOUR, FONT)

        # Events when the player collects all the cogs
        if cog_score == final_cog_score:
            cogspawn_interval = 0
            cogs = []
            if len(debris) == 0:
                if draw_weapon:
                    spawn_weapon()
                    weapon.draw(canvas)
                if player.collide(weapon):
                    draw_cont_button = True

        # Draws button on screen
        if draw_cont_button:
            draw_continue_button()
            cont_button.draw(canvas)

            # Instructions for stage 2
            canvas.draw_text("The aliens are here! Use the arrows keys to move left and right, and",
                             CONT_TEXT_POS1, CONT_TEXT_SIZE,
                             TEXT_COLOUR, FONT)
            canvas.draw_text("shoot bullets at them using the spacebar before they destroy the planet!",
                             CONT_TEXT_POS2, CONT_TEXT_SIZE,
                             TEXT_COLOUR, FONT)
            canvas.draw_text("Be careful though; some may need to be shot multiple times to kill them.",
                             CONT_TEXT_POS3, CONT_TEXT_SIZE,
                             TEXT_COLOUR, FONT)

    # Stage 2 - Moving spaceship and fighting
    if stage == STAGE2:

        # Draw and update player
        player.draw(canvas)
        player.update()

        # Tells player their health
        canvas.draw_text("Health: " + str(player_health),
                         HEALTH_LABEL_POS, LABEL_SIZE,
                         LABEL_COLOUR, FONT)
        # Draws enemy
        if start_spawn_enemy:
            enemy_timer.start()
            for enemy in enemies:
                enemy.draw(canvas)
                enemy.update()
                # Decreases player health when the enemy gets past
                if enemy.pos[1] == BOUNDARY:
                    player_health -= enemy.attack
                    enemies_passed += 1

        # Draws bullets on screen
        for bullet in bullets:
            bullet.draw(canvas)
            bullet.pos[1] += bullet_speed
            if bullet.pos[1] <= 0:
                bullets.remove(bullet)
                return

            # If the enemy collides with the bullet, remove both
            for enemy in enemies:
                if enemy.collide_y(bullet):
                    bullets.remove(bullet)
                    enemy.health -= 1
                    if enemy.health == 0:
                        enemies.remove(enemy)
                        enemies_killed += 1
                        enemies_points += enemy.points
                continue
        if player_health <= 0:
            game_over()

    # Stage 3 - Game Over screen and stats
    if stage == GAMEOVER:
        if draw_replay:
            draw_replay_button()
            replay_button.draw(canvas)

        # Gameover message
        canvas.draw_text("Your spaceship was damaged again and the aliens have invaded but there's still hope! ",
                         GAMEOVER_LINE1_POS, TEXT_SIZE, TEXT_COLOUR, FONT)
        canvas.draw_text("Try again and save the planet!",
                         GAMEOVER_LINE2_POS, TEXT_SIZE, TEXT_COLOUR, FONT)

        # Setting value of high score
        if enemies_points > high_score:
            high_score = enemies_points

        # Stats
        canvas.draw_text(str(bullets_shot) + " bullets shot",
                         BULLETS_SHOT_POS, STATS_SIZE, TEXT_COLOUR, FONT)
        canvas.draw_text(str(enemies_killed) + " enemies killed",
                         ENEMIES_KILLED_POS, STATS_SIZE, TEXT_COLOUR, FONT)
        canvas.draw_text(str(enemies_passed) + " enemies got past",
                         ENEMIES_PASSED_POS, STATS_SIZE, TEXT_COLOUR, FONT)
        canvas.draw_text(str(enemies_points) + " points",
                         ENEMIES_POINTS_POS, POINTS_LABEL_SIZE, LABEL_COLOUR, FONT)
        canvas.draw_text("High Score: " + str(high_score),
                         HIGH_SCORE_POS, LABEL_SIZE, TEXT_COLOUR, FONT)


# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", FRAME_WIDTH, FRAME_HEIGHT)

# Handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_press)
frame.set_keyup_handler(key_release)
frame.set_mouseclick_handler(mouse_click)

# Timer
enemy_timer = simplegui.create_timer(time_interval, spawn_enemy)

# Start the frame animation
start_screen()
frame.start()
