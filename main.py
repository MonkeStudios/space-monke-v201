@namespace
class SpriteKind:
    background = SpriteKind.create()

def on_on_created(sprite):
    sprite.set_velocity(-50, 0)
    sprite.set_flag(SpriteFlag.AUTO_DESTROY, True)
sprites.on_created(SpriteKind.enemy, on_on_created)

def on_player2_button_b_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(assets.image("""
        sharky
    """), mySprite2, -50, 0)
    music.rest(music.beat(BeatFraction.WHOLE))
controller.player2.on_button_event(ControllerButton.B,
    ControllerButtonEvent.PRESSED,
    on_player2_button_b_pressed)

def on_b_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . c c c c . . . . 
                    . . . . c c c c c c c c c . . . 
                    . . . c f c c a a a a c a c . . 
                    . . c c f f f f a a a c a a c . 
                    . . c c a f f c a a f f f a a c 
                    . . c c a a a a b c f f f a a c 
                    . c c c c a c c b a f c a a c c 
                    c a f f c c c a b b 6 b b b c c 
                    c a f f f f c c c 6 b b b a a c 
                    c a a c f f c a 6 6 b b b a a c 
                    c c b a a a a b 6 b b a b b a . 
                    . c c b b b b b b b a c c b a . 
                    . . c c c b c c c b a a b c . . 
                    . . . . c b a c c b b b c . . . 
                    . . . . c b b a a 6 b c . . . . 
                    . . . . . . b 6 6 c c . . . . .
        """),
        mySprite,
        -60,
        0)
    music.rest(music.beat(BeatFraction.BREVE))
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . c c c c . . . . 
                    . . . . c c c c c c c c c . . . 
                    . . . c f c c a a a a c a c . . 
                    . . c c f f f f a a a c a a c . 
                    . . c c a f f c a a f f f a a c 
                    . . c c a a a a b c f f f a a c 
                    . c c c c a c c b a f c a a c c 
                    c a f f c c c a b b 6 b b b c c 
                    c a f f f f c c c 6 b b b a a c 
                    c a a c f f c a 6 6 b b b a a c 
                    c c b a a a a b 6 b b a b b a . 
                    . c c b b b b b b b a c c b a . 
                    . . c c c b c c c b a a b c . . 
                    . . . . c b a c c b b b c . . . 
                    . . . . c b b a a 6 b c . . . . 
                    . . . . . . b 6 6 c c . . . . .
        """),
        mySprite,
        60,
        0)
    music.rest(music.beat(BeatFraction.WHOLE))
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_player2_button_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(assets.image("""
        sharky
    """), mySprite2, 50, 0)
controller.player2.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player2_button_a_pressed)

def on_player2_connected():
    global mySprite2
    mySprite2 = sprites.create(assets.image("""
        Playah too
    """), SpriteKind.player)
    controller.player2.move_sprite(mySprite2)
controller.player2.on_event(ControllerEvent.CONNECTED, on_player2_connected)

def on_on_destroyed(sprite):
    game.over(False)
sprites.on_destroyed(SpriteKind.player, on_on_destroyed)

def on_on_overlap(sprite, otherSprite):
    otherSprite.destroy()
    sprite.destroy()
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    mySprite.destroy()
    game.over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

enemySprite: Sprite = None
mySprite2: Sprite = None
projectile: Sprite = None
mySprite: Sprite = None
scene.set_background_image(assets.image("""
    sky
"""))
scene.set_background_color(10)
mySprite = sprites.create(assets.image("""
    space monke
"""), SpriteKind.player)
controller.move_sprite(mySprite)
mySprite.set_stay_in_screen(True)

def on_forever():
    music.play_melody("C5 B - A - B C5 - ", 250)
forever(on_forever)

def on_forever2():
    global projectile
    if controller.A.is_pressed() and controller.B.is_pressed() and (not (controller.up.is_pressed()) and not (controller.down.is_pressed()) and (not (controller.right.is_pressed()) and not (controller.left.is_pressed()))):
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . c c c c . . . . 
                            . . . . c c c c c c c c c . . . 
                            . . . c f c c a a a a c a c . . 
                            . . c c f f f f a a a c a a c . 
                            . . c c a f f c a a f f f a a c 
                            . . c c a a a a b c f f f a a c 
                            . c c c c a c c b a f c a a c c 
                            c a f f c c c a b b 6 b b b c c 
                            c a f f f f c c c 6 b b b a a c 
                            c a a c f f c a 6 6 b b b a a c 
                            c c b a a a a b 6 b b a b b a . 
                            . c c b b b b b b b a c c b a . 
                            . . c c c b c c c b a a b c . . 
                            . . . . c b a c c b b b c . . . 
                            . . . . c b b a a 6 b c . . . . 
                            . . . . . . b 6 6 c c . . . . .
            """),
            mySprite,
            60,
            0)
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . c c c c . . . . 
                            . . . . c c c c c c c c c . . . 
                            . . . c f c c a a a a c a c . . 
                            . . c c f f f f a a a c a a c . 
                            . . c c a f f c a a f f f a a c 
                            . . c c a a a a b c f f f a a c 
                            . c c c c a c c b a f c a a c c 
                            c a f f c c c a b b 6 b b b c c 
                            c a f f f f c c c 6 b b b a a c 
                            c a a c f f c a 6 6 b b b a a c 
                            c c b a a a a b 6 b b a b b a . 
                            . c c b b b b b b b a c c b a . 
                            . . c c c b c c c b a a b c . . 
                            . . . . c b a c c b b b c . . . 
                            . . . . c b b a a 6 b c . . . . 
                            . . . . . . b 6 6 c c . . . . .
            """),
            mySprite,
            -60,
            0)
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . c c c c . . . . 
                            . . . . c c c c c c c c c . . . 
                            . . . c f c c a a a a c a c . . 
                            . . c c f f f f a a a c a a c . 
                            . . c c a f f c a a f f f a a c 
                            . . c c a a a a b c f f f a a c 
                            . c c c c a c c b a f c a a c c 
                            c a f f c c c a b b 6 b b b c c 
                            c a f f f f c c c 6 b b b a a c 
                            c a a c f f c a 6 6 b b b a a c 
                            c c b a a a a b 6 b b a b b a . 
                            . c c b b b b b b b a c c b a . 
                            . . c c c b c c c b a a b c . . 
                            . . . . c b a c c b b b c . . . 
                            . . . . c b b a a 6 b c . . . . 
                            . . . . . . b 6 6 c c . . . . .
            """),
            mySprite,
            0,
            60)
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . c c c c . . . . 
                            . . . . c c c c c c c c c . . . 
                            . . . c f c c a a a a c a c . . 
                            . . c c f f f f a a a c a a c . 
                            . . c c a f f c a a f f f a a c 
                            . . c c a a a a b c f f f a a c 
                            . c c c c a c c b a f c a a c c 
                            c a f f c c c a b b 6 b b b c c 
                            c a f f f f c c c 6 b b b a a c 
                            c a a c f f c a 6 6 b b b a a c 
                            c c b a a a a b 6 b b a b b a . 
                            . c c b b b b b b b a c c b a . 
                            . . c c c b c c c b a a b c . . 
                            . . . . c b a c c b b b c . . . 
                            . . . . c b b a a 6 b c . . . . 
                            . . . . . . b 6 6 c c . . . . .
            """),
            mySprite,
            0,
            -60)
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . c c c c . . . . 
                            . . . . c c c c c c c c c . . . 
                            . . . c f c c a a a a c a c . . 
                            . . c c f f f f a a a c a a c . 
                            . . c c a f f c a a f f f a a c 
                            . . c c a a a a b c f f f a a c 
                            . c c c c a c c b a f c a a c c 
                            c a f f c c c a b b 6 b b b c c 
                            c a f f f f c c c 6 b b b a a c 
                            c a a c f f c a 6 6 b b b a a c 
                            c c b a a a a b 6 b b a b b a . 
                            . c c b b b b b b b a c c b a . 
                            . . c c c b c c c b a a b c . . 
                            . . . . c b a c c b b b c . . . 
                            . . . . c b b a a 6 b c . . . . 
                            . . . . . . b 6 6 c c . . . . .
            """),
            mySprite,
            30,
            30)
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . c c c c . . . . 
                            . . . . c c c c c c c c c . . . 
                            . . . c f c c a a a a c a c . . 
                            . . c c f f f f a a a c a a c . 
                            . . c c a f f c a a f f f a a c 
                            . . c c a a a a b c f f f a a c 
                            . c c c c a c c b a f c a a c c 
                            c a f f c c c a b b 6 b b b c c 
                            c a f f f f c c c 6 b b b a a c 
                            c a a c f f c a 6 6 b b b a a c 
                            c c b a a a a b 6 b b a b b a . 
                            . c c b b b b b b b a c c b a . 
                            . . c c c b c c c b a a b c . . 
                            . . . . c b a c c b b b c . . . 
                            . . . . c b b a a 6 b c . . . . 
                            . . . . . . b 6 6 c c . . . . .
            """),
            mySprite,
            30,
            -30)
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . c c c c . . . . 
                            . . . . c c c c c c c c c . . . 
                            . . . c f c c a a a a c a c . . 
                            . . c c f f f f a a a c a a c . 
                            . . c c a f f c a a f f f a a c 
                            . . c c a a a a b c f f f a a c 
                            . c c c c a c c b a f c a a c c 
                            c a f f c c c a b b 6 b b b c c 
                            c a f f f f c c c 6 b b b a a c 
                            c a a c f f c a 6 6 b b b a a c 
                            c c b a a a a b 6 b b a b b a . 
                            . c c b b b b b b b a c c b a . 
                            . . c c c b c c c b a a b c . . 
                            . . . . c b a c c b b b c . . . 
                            . . . . c b b a a 6 b c . . . . 
                            . . . . . . b 6 6 c c . . . . .
            """),
            mySprite,
            -30,
            30)
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . c c c c . . . . 
                            . . . . c c c c c c c c c . . . 
                            . . . c f c c a a a a c a c . . 
                            . . c c f f f f a a a c a a c . 
                            . . c c a f f c a a f f f a a c 
                            . . c c a a a a b c f f f a a c 
                            . c c c c a c c b a f c a a c c 
                            c a f f c c c a b b 6 b b b c c 
                            c a f f f f c c c 6 b b b a a c 
                            c a a c f f c a 6 6 b b b a a c 
                            c c b a a a a b 6 b b a b b a . 
                            . c c b b b b b b b a c c b a . 
                            . . c c c b c c c b a a b c . . 
                            . . . . c b a c c b b b c . . . 
                            . . . . c b b a a 6 b c . . . . 
                            . . . . . . b 6 6 c c . . . . .
            """),
            mySprite,
            -30,
            -30)
        music.rest(music.beat(BeatFraction.BREVE))
        music.rest(music.beat(BeatFraction.BREVE))
    if controller.A.is_pressed() and controller.B.is_pressed() and controller.right.is_pressed():
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . c c c c . . . . 
                            . . . . c c c c c c c c c . . . 
                            . . . c f c c a a a a c a c . . 
                            . . c c f f f f a a a c a a c . 
                            . . c c a f f c a a f f f a a c 
                            . . c c a a a a b c f f f a a c 
                            . c c c c a c c b a f c a a c c 
                            c a f f c c c a b b 6 b b b c c 
                            c a f f f f c c c 6 b b b a a c 
                            c a a c f f c a 6 6 b b b a a c 
                            c c b a a a a b 6 b b a b b a . 
                            . c c b b b b b b b a c c b a . 
                            . . c c c b c c c b a a b c . . 
                            . . . . c b a c c b b b c . . . 
                            . . . . c b b a a 6 b c . . . . 
                            . . . . . . b 6 6 c c . . . . .
            """),
            mySprite,
            60,
            0)
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . c c c c . . . . 
                            . . . . c c c c c c c c c . . . 
                            . . . c f c c a a a a c a c . . 
                            . . c c f f f f a a a c a a c . 
                            . . c c a f f c a a f f f a a c 
                            . . c c a a a a b c f f f a a c 
                            . c c c c a c c b a f c a a c c 
                            c a f f c c c a b b 6 b b b c c 
                            c a f f f f c c c 6 b b b a a c 
                            c a a c f f c a 6 6 b b b a a c 
                            c c b a a a a b 6 b b a b b a . 
                            . c c b b b b b b b a c c b a . 
                            . . c c c b c c c b a a b c . . 
                            . . . . c b a c c b b b c . . . 
                            . . . . c b b a a 6 b c . . . . 
                            . . . . . . b 6 6 c c . . . . .
            """),
            mySprite,
            30,
            30)
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . c c c c . . . . 
                            . . . . c c c c c c c c c . . . 
                            . . . c f c c a a a a c a c . . 
                            . . c c f f f f a a a c a a c . 
                            . . c c a f f c a a f f f a a c 
                            . . c c a a a a b c f f f a a c 
                            . c c c c a c c b a f c a a c c 
                            c a f f c c c a b b 6 b b b c c 
                            c a f f f f c c c 6 b b b a a c 
                            c a a c f f c a 6 6 b b b a a c 
                            c c b a a a a b 6 b b a b b a . 
                            . c c b b b b b b b a c c b a . 
                            . . c c c b c c c b a a b c . . 
                            . . . . c b a c c b b b c . . . 
                            . . . . c b b a a 6 b c . . . . 
                            . . . . . . b 6 6 c c . . . . .
            """),
            mySprite,
            30,
            -30)
        music.rest(music.beat(BeatFraction.BREVE))
        music.rest(music.beat(BeatFraction.WHOLE))
    if controller.A.is_pressed() and controller.B.is_pressed() and controller.left.is_pressed():
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . c c c c . . . . 
                            . . . . c c c c c c c c c . . . 
                            . . . c f c c a a a a c a c . . 
                            . . c c f f f f a a a c a a c . 
                            . . c c a f f c a a f f f a a c 
                            . . c c a a a a b c f f f a a c 
                            . c c c c a c c b a f c a a c c 
                            c a f f c c c a b b 6 b b b c c 
                            c a f f f f c c c 6 b b b a a c 
                            c a a c f f c a 6 6 b b b a a c 
                            c c b a a a a b 6 b b a b b a . 
                            . c c b b b b b b b a c c b a . 
                            . . c c c b c c c b a a b c . . 
                            . . . . c b a c c b b b c . . . 
                            . . . . c b b a a 6 b c . . . . 
                            . . . . . . b 6 6 c c . . . . .
            """),
            mySprite,
            -60,
            0)
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . c c c c . . . . 
                            . . . . c c c c c c c c c . . . 
                            . . . c f c c a a a a c a c . . 
                            . . c c f f f f a a a c a a c . 
                            . . c c a f f c a a f f f a a c 
                            . . c c a a a a b c f f f a a c 
                            . c c c c a c c b a f c a a c c 
                            c a f f c c c a b b 6 b b b c c 
                            c a f f f f c c c 6 b b b a a c 
                            c a a c f f c a 6 6 b b b a a c 
                            c c b a a a a b 6 b b a b b a . 
                            . c c b b b b b b b a c c b a . 
                            . . c c c b c c c b a a b c . . 
                            . . . . c b a c c b b b c . . . 
                            . . . . c b b a a 6 b c . . . . 
                            . . . . . . b 6 6 c c . . . . .
            """),
            mySprite,
            -30,
            30)
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . c c c c . . . . 
                            . . . . c c c c c c c c c . . . 
                            . . . c f c c a a a a c a c . . 
                            . . c c f f f f a a a c a a c . 
                            . . c c a f f c a a f f f a a c 
                            . . c c a a a a b c f f f a a c 
                            . c c c c a c c b a f c a a c c 
                            c a f f c c c a b b 6 b b b c c 
                            c a f f f f c c c 6 b b b a a c 
                            c a a c f f c a 6 6 b b b a a c 
                            c c b a a a a b 6 b b a b b a . 
                            . c c b b b b b b b a c c b a . 
                            . . c c c b c c c b a a b c . . 
                            . . . . c b a c c b b b c . . . 
                            . . . . c b b a a 6 b c . . . . 
                            . . . . . . b 6 6 c c . . . . .
            """),
            mySprite,
            -30,
            -30)
        music.rest(music.beat(BeatFraction.BREVE))
        music.rest(music.beat(BeatFraction.WHOLE))
    if controller.A.is_pressed() and controller.B.is_pressed() and controller.down.is_pressed():
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . c c c c . . . . 
                            . . . . c c c c c c c c c . . . 
                            . . . c f c c a a a a c a c . . 
                            . . c c f f f f a a a c a a c . 
                            . . c c a f f c a a f f f a a c 
                            . . c c a a a a b c f f f a a c 
                            . c c c c a c c b a f c a a c c 
                            c a f f c c c a b b 6 b b b c c 
                            c a f f f f c c c 6 b b b a a c 
                            c a a c f f c a 6 6 b b b a a c 
                            c c b a a a a b 6 b b a b b a . 
                            . c c b b b b b b b a c c b a . 
                            . . c c c b c c c b a a b c . . 
                            . . . . c b a c c b b b c . . . 
                            . . . . c b b a a 6 b c . . . . 
                            . . . . . . b 6 6 c c . . . . .
            """),
            mySprite,
            0,
            60)
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . c c c c . . . . 
                            . . . . c c c c c c c c c . . . 
                            . . . c f c c a a a a c a c . . 
                            . . c c f f f f a a a c a a c . 
                            . . c c a f f c a a f f f a a c 
                            . . c c a a a a b c f f f a a c 
                            . c c c c a c c b a f c a a c c 
                            c a f f c c c a b b 6 b b b c c 
                            c a f f f f c c c 6 b b b a a c 
                            c a a c f f c a 6 6 b b b a a c 
                            c c b a a a a b 6 b b a b b a . 
                            . c c b b b b b b b a c c b a . 
                            . . c c c b c c c b a a b c . . 
                            . . . . c b a c c b b b c . . . 
                            . . . . c b b a a 6 b c . . . . 
                            . . . . . . b 6 6 c c . . . . .
            """),
            mySprite,
            -30,
            30)
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . c c c c . . . . 
                            . . . . c c c c c c c c c . . . 
                            . . . c f c c a a a a c a c . . 
                            . . c c f f f f a a a c a a c . 
                            . . c c a f f c a a f f f a a c 
                            . . c c a a a a b c f f f a a c 
                            . c c c c a c c b a f c a a c c 
                            c a f f c c c a b b 6 b b b c c 
                            c a f f f f c c c 6 b b b a a c 
                            c a a c f f c a 6 6 b b b a a c 
                            c c b a a a a b 6 b b a b b a . 
                            . c c b b b b b b b a c c b a . 
                            . . c c c b c c c b a a b c . . 
                            . . . . c b a c c b b b c . . . 
                            . . . . c b b a a 6 b c . . . . 
                            . . . . . . b 6 6 c c . . . . .
            """),
            mySprite,
            30,
            30)
        music.rest(music.beat(BeatFraction.BREVE))
        music.rest(music.beat(BeatFraction.WHOLE))
    if controller.A.is_pressed() and controller.B.is_pressed() and controller.up.is_pressed():
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . c c c c . . . . 
                            . . . . c c c c c c c c c . . . 
                            . . . c f c c a a a a c a c . . 
                            . . c c f f f f a a a c a a c . 
                            . . c c a f f c a a f f f a a c 
                            . . c c a a a a b c f f f a a c 
                            . c c c c a c c b a f c a a c c 
                            c a f f c c c a b b 6 b b b c c 
                            c a f f f f c c c 6 b b b a a c 
                            c a a c f f c a 6 6 b b b a a c 
                            c c b a a a a b 6 b b a b b a . 
                            . c c b b b b b b b a c c b a . 
                            . . c c c b c c c b a a b c . . 
                            . . . . c b a c c b b b c . . . 
                            . . . . c b b a a 6 b c . . . . 
                            . . . . . . b 6 6 c c . . . . .
            """),
            mySprite,
            0,
            -60)
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . c c c c . . . . 
                            . . . . c c c c c c c c c . . . 
                            . . . c f c c a a a a c a c . . 
                            . . c c f f f f a a a c a a c . 
                            . . c c a f f c a a f f f a a c 
                            . . c c a a a a b c f f f a a c 
                            . c c c c a c c b a f c a a c c 
                            c a f f c c c a b b 6 b b b c c 
                            c a f f f f c c c 6 b b b a a c 
                            c a a c f f c a 6 6 b b b a a c 
                            c c b a a a a b 6 b b a b b a . 
                            . c c b b b b b b b a c c b a . 
                            . . c c c b c c c b a a b c . . 
                            . . . . c b a c c b b b c . . . 
                            . . . . c b b a a 6 b c . . . . 
                            . . . . . . b 6 6 c c . . . . .
            """),
            mySprite,
            30,
            -30)
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . c c c c . . . . 
                            . . . . c c c c c c c c c . . . 
                            . . . c f c c a a a a c a c . . 
                            . . c c f f f f a a a c a a c . 
                            . . c c a f f c a a f f f a a c 
                            . . c c a a a a b c f f f a a c 
                            . c c c c a c c b a f c a a c c 
                            c a f f c c c a b b 6 b b b c c 
                            c a f f f f c c c 6 b b b a a c 
                            c a a c f f c a 6 6 b b b a a c 
                            c c b a a a a b 6 b b a b b a . 
                            . c c b b b b b b b a c c b a . 
                            . . c c c b c c c b a a b c . . 
                            . . . . c b a c c b b b c . . . 
                            . . . . c b b a a 6 b c . . . . 
                            . . . . . . b 6 6 c c . . . . .
            """),
            mySprite,
            -30,
            -30)
        music.rest(music.beat(BeatFraction.BREVE))
        music.rest(music.beat(BeatFraction.WHOLE))
forever(on_forever2)

def on_update_interval():
    global enemySprite
    enemySprite = sprites.create(assets.image("""
        broccoli
    """), SpriteKind.enemy)
    enemySprite.set_position(randint(125, 160), randint(0, 105))
game.on_update_interval(500, on_update_interval)
