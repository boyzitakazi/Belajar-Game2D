# Library yang diperlukan
import pygame
import sys
import time
import random

# untuk manampilkan screen lebar 1000 tinggi 600
pygame.display.init()
win = pygame.display.set_mode((1000, 600))

# Judul game
pygame.display.set_caption("Namain Sendiri Gamenya")

# Menambahkan gambar dari assets
deathBackground1 = pygame.image.load("env/deathHollow/BG1.png")
deathBackground2 = pygame.image.load("env/deathHollow/BG2.png")
deathChurch = pygame.image.load("env/deathHollow/Church.png")
deathMoon = [pygame.image.load("env/deathHollow/M1.png"),pygame.image.load("env/deathHollow/M2.png"),pygame.image.load("env/deathHollow/M3.png"),pygame.image.load("env/deathHollow/M4.png"),pygame.image.load("env/deathHollow/M5.png"),pygame.image.load("env/deathHollow/M6.png"),pygame.image.load("env/deathHollow/M7.png"),pygame.image.load("env/deathHollow/M8.png")]
deathCstoon = pygame.image.load("env/deathHollow/pl_center.png")
deathLstoon = pygame.image.load("env/deathHollow/pl_left.png")
deathRstoon = pygame.image.load("env/deathHollow/pl_right.png")
deathWater = [pygame.image.load("env/deathHollow/W1.png"),pygame.image.load("env/deathHollow/W2.png"),pygame.image.load("env/deathHollow/W3.png"),pygame.image.load("env/deathHollow/W4.png"),pygame.image.load("env/deathHollow/W5.png"),pygame.image.load("env/deathHollow/W6.png"),pygame.image.load("env/deathHollow/W7.png"),pygame.image.load("env/deathHollow/W8.png")]
deathGrave1 = pygame.image.load("env/deathHollow/G1.png")
deathGrave2 = pygame.image.load("env/deathHollow/G2.png")
deathGrave3 = pygame.image.load("env/deathHollow/G3.png")
deathLadder = pygame.image.load("env/deathHollow/Ladder.png")
deathFire = [pygame.image.load("env/deathHollow/F1.png"),pygame.image.load("env/deathHollow/F2.png"),pygame.image.load("env/deathHollow/F3.png"),pygame.image.load("env/deathHollow/F4.png"),pygame.image.load("env/deathHollow/F5.png"),pygame.image.load("env/deathHollow/F6.png"),pygame.image.load("env/deathHollow/F7.png"),pygame.image.load("env/deathHollow/F8.png")]
deathMist = pygame.image.load("env/deathHollow/Mist.png")
deathTree = pygame.image.load("env/deathHollow/Tree.png")
deathUcenter = pygame.image.load("env/deathHollow/up_center.png")
deathUleft = pygame.image.load("env/deathHollow/up_left.png")
deathUright = pygame.image.load("env/deathHollow/up_right.png")

# Fire Sprite 
fireSprite = [pygame.image.load("env/fire/F1.png"),pygame.image.load("env/fire/F2.png"),pygame.image.load("env/fire/F3.png"),pygame.image.load("env/fire/F4.png"),pygame.image.load("env/fire/F5.png"),pygame.image.load("env/fire/F6.png"),pygame.image.load("env/fire/F7.png"),pygame.image.load("env/fire/F8.png"),pygame.image.load("env/fire/F9.png"),pygame.image.load("env/fire/F10.png"),pygame.image.load("env/fire/F11.png"),pygame.image.load("env/fire/F12.png"), pygame.image.load("env/fire/F13.png"),pygame.image.load("env/fire/F14.png"),pygame.image.load("env/fire/F15.png"),pygame.image.load("env/fire/F16.png")]

# Sword Giant
swordSprite = [pygame.image.load("env/sword/S1.png"),pygame.image.load("env/sword/S2.png"), pygame.image.load("env/sword/S3.png"), pygame.image.load("env/sword/S4.png"), pygame.image.load("env/sword/S5.png"), pygame.image.load("env/sword/S6.png"), pygame.image.load("env/sword/S7.png"), pygame.image.load("env/sword/S8.png"), pygame.image.load("env/sword/S9.png"),pygame.image.load("env/sword/S10.png"), pygame.image.load("env/sword/S11.png"), pygame.image.load("env/sword/S12.png"), pygame.image.load("env/sword/S13.png"), pygame.image.load("env/sword/S14.png"), pygame.image.load("env/sword/S15.png"),pygame.image.load("env/sword/S16.png"), pygame.image.load("env/sword/S17.png"), pygame.image.load("env/sword/S18.png"), pygame.image.load("env/sword/S19.png"), pygame.image.load("env/sword/S20.png"), pygame.image.load("env/sword/S21.png"), pygame.image.load("env/sword/S22.png"), pygame.image.load("env/sword/S23.png"), pygame.image.load("env/sword/S24.png"), pygame.image.load("env/sword/S25.png"), pygame.image.load("env/sword/S26.png"), pygame.image.load("env/sword/S27.png"), pygame.image.load("env/sword/S28.png"), pygame.image.load("env/sword/S29.png"),pygame.image.load("env/sword/S30.png"), pygame.image.load("env/sword/S31.png"), pygame.image.load("env/sword/S32.png"), pygame.image.load("env/sword/S33.png"), pygame.image.load("env/sword/S34.png"), pygame.image.load("env/sword/S35.png"), pygame.image.load("env/sword/S36.png"), pygame.image.load("env/sword/S37.png"), pygame.image.load("env/sword/S38.png"), pygame.image.load("env/sword/S39.png"), pygame.image.load("env/sword/S40.png")]

# Hero IDLE/ kondisi haro tidak bergerak
idleSprite = [pygame.image.load("hero/idle/I1.png"),pygame.image.load("hero/idle/I2.png"),pygame.image.load("hero/idle/I3.png"),pygame.image.load("hero/idle/I4.png"),pygame.image.load("hero/idle/I5.png"),pygame.image.load("hero/idle/I6.png"),pygame.image.load("hero/idle/I7.png"),pygame.image.load("hero/idle/I8.png")]

# Hero Run
heroRunSprite = [pygame.image.load("hero/run/P1.png"),pygame.image.load("hero/run/P2.png"),pygame.image.load("hero/run/P3.png"),pygame.image.load("hero/run/P4.png"),pygame.image.load("hero/run/P5.png"),pygame.image.load("hero/run/P6.png"),pygame.image.load("hero/run/P7.png"),pygame.image.load("hero/run/P8.png")]

# Hero Attack
swingAttackSprite = [pygame.image.load("hero/swingAttack/SA1.png"), pygame.image.load("hero/swingAttack/SA2.png"),pygame.image.load("hero/swingAttack/SA3.png"),pygame.image.load("hero/swingAttack/SA4.png"),pygame.image.load("hero/swingAttack/SA5.png"),pygame.image.load("hero/swingAttack/SA6.png"),pygame.image.load("hero/swingAttack/SA7.png"),pygame.image.load("hero/swingAttack/SA8.png"),pygame.image.load("hero/swingAttack/SA9.png"),pygame.image.load("hero/swingAttack/SA10.png"),pygame.image.load("hero/swingAttack/SA11.png"),pygame.image.load("hero/swingAttack/SA12.png")]

# Mengubah Ukuran Assets
# ukuran deathUcenter
deathUcenterTransform = pygame.transform.scale(deathUcenter, (1000, 200))

# ukuran hero idle
listIdlePlayer = []
for i in range(0,8):
    player = pygame.transform.scale(idleSprite[i], (100, 100))
    listIdlePlayer.append(player)

# ukuran hero run
listRunPlayer = []
for i in range(0,8):
    player = pygame.transform.scale(heroRunSprite[i], (100, 100))
    listRunPlayer.append(player)

# ukuran hero attack
listSwingAttack = []
for i in range(0,12):
    player = pygame.transform.scale(swingAttackSprite[i], (100, 100))
    listSwingAttack.append(player)


# posisi hero dan ukuran hero
x = 100
y = 380
vel = 5
width = 64
height = 64

# logika untuk hero loncat
isJump = False
jumpCount = 10

# logika untuk hero berjalan
left = False
right = False
walkCount = 0

# untuk 
bgCount = 0

# FPS/kecepatan pergerakan hero
clock = pygame.time.Clock()

# daftar fungsi fungsi
def death():
    global y, x

    if y == 0:
        y = 380
    if x >= 720 or y >= 500:
        y += 20
    if y >= 460:
        x = 0
        y = 380

def renDrawScreen():
    global walkCount
    global bgCount

    if walkCount + 1 >= 16:
        walkCount = 0
    if bgCount + 1 >= 16:
        bgCount = 0

    if left:
        win.blit(listRunPlayer[walkCount//2], (x,y))
        walkCount += 1
    elif right:
        win.blit(listRunPlayer[walkCount//2], (x,y))
        walkCount += 1
    else:
        win.blit(listIdlePlayer[bgCount//2], (x,y))
        bgCount += 1
    
def attack():
    global bgCount
    if bgCount + 1 >= 24:
        bgCount = 0
    win.blit(listSwingAttack[bgCount//2], (x,y))
    bgCount += 1

def fire():
    global bgCount
    if bgCount + 1 >= 32:
        bgCount = 0
    
    win.blit(fireSprite[bgCount//2], (50,410))
    bgCount += 1

def background():
    for i in range(14,20):
        win.blit(deathUcenterTransform, (deathUcenter.get_width()*i, 380))
    win.blit(deathUleft, (deathUcenter.get_width()*14, 380))
    win.blit(deathUleft, (deathUcenter.get_width()*14, 400))
    win.blit(deathUleft, (deathUcenter.get_width()*14, 420))
    win.blit(deathUleft, (deathUcenter.get_width()*14, 440))
    for i in range(0,3):
        win.blit(deathBackground1, (deathBackground1.get_width()*i, 400))

    for i in range(14,20):
        win.blit(deathCstoon, (deathCstoon.get_width()*i, 350))
        win.blit(deathLstoon, (deathCstoon.get_width()*14, 350))

    for i in range(0,14):
        win.blit(deathCstoon, (deathCstoon.get_width()*i, 455))
        win.blit(deathRstoon, (deathCstoon.get_width()*14, 455))

    win.blit(deathUcenterTransform, (0, 489))
    win.blit(deathUright, (deathUcenter.get_width()*14, 488))
    win.blit(deathUright, (deathUcenter.get_width()*14, 490))
    win.blit(deathUright, (deathUcenter.get_width()*14, 500))
    win.blit(deathUright, (deathUcenter.get_width()*14, 520))
    win.blit(deathUright, (deathUcenter.get_width()*14, 540))

def water():
    global bgCount
    if bgCount + 1 >= 16:
        bgCount = 0
    for i in range(0,7):
        win.blit(deathWater[bgCount//2], (deathWater[0].get_width()*i, 565))

def giantSword():
    global bgCount
    if bgCount + 1 >= 80:
        bgCount = 0
    win.blit(swordSprite[bgCount//2], (swordSprite[0].get_width(), 455))
    bgCount += 1

while 1:
    clock.tick(27)
    win.fill((0,0,0))
    background()
    fire()
    water()
    giantSword()

    # kondisi keluar dari game
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # membaca input dari user
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 1000 - width - vel:
        x += vel
        left = False
        right = True
    elif keys[pygame.K_g]:
        left = False
        right = False
        walkCount = 0
        attack()
    else:
        left = False
        right = False
        walkCount = 0
    
    # logika untuk loncat
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False

    renDrawScreen()
    death()

    # UPDATE SCREEN
    pygame.display.update()
    
pygame.display.quit()
quit()