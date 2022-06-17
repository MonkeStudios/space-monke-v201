namespace SpriteKind {
    export const background = SpriteKind.create()
    export const Boss = SpriteKind.create()
    export const Enemy2 = SpriteKind.create()
    export const Enemy3 = SpriteKind.create()
    export const Enemy4 = SpriteKind.create()
    export const PowerUp1 = SpriteKind.create()
    export const PowerUp2 = SpriteKind.create()
    export const PowerUp3 = SpriteKind.create()
    export const PowerUp4 = SpriteKind.create()
    export const PowerUp5 = SpriteKind.create()
    export const PowerUp6 = SpriteKind.create()
    export const PowerUp7 = SpriteKind.create()
    export const Shield = SpriteKind.create()
    export const HeatSeeker = SpriteKind.create()
    export const BouncyBlueberry = SpriteKind.create()
    export const BouncyOrange = SpriteKind.create()
}
sprites.onCreated(SpriteKind.Enemy, function (sprite) {
    sprite.setVelocity(-50, 0)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.PowerUp2, function (sprite, otherSprite) {
    otherSprite.destroy()
    controller.moveSprite(Player1Monke, 50, 50)
    pause(10000)
    controller.moveSprite(Player1Monke, 100, 100)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy4, function (sprite, otherSprite) {
    otherSprite.destroy()
    sprite.destroy()
    info.changeScoreBy(10)
})
sprites.onOverlap(SpriteKind.Enemy4, SpriteKind.Shield, function (sprite, otherSprite) {
    sprite.destroy()
    info.changeScoreBy(10)
})
sprites.onCreated(SpriteKind.BouncyOrange, function (sprite) {
    sprite.setVelocity(-50, 25)
})
sprites.onOverlap(SpriteKind.Boss, SpriteKind.Shield, function (sprite, otherSprite) {
    sprite.destroy()
    Boss_Lives = 3
    info.changeScoreBy(4)
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    if (BackAttack == 4) {
        if (bTime == 0) {
            bTime = 72
            projectile = sprites.createProjectileFromSprite(assets.image`Space Monke Projectile`, Player1Monke, -120, 0)
            projectile = sprites.createProjectileFromSprite(assets.image`Space Monke Projectile`, Player1Monke, -120, 25)
            projectile = sprites.createProjectileFromSprite(assets.image`Space Monke Projectile`, Player1Monke, -120, -25)
        }
    } else {
        if (BackAttack == 3) {
            if (bTime == 0) {
                bTime = 72
                projectile = sprites.createProjectileFromSprite(assets.image`Tiny Pizza`, Player1Monke, -120, 0)
            }
        } else {
            if (BackAttack == 2) {
                if (bTime == 0) {
                    bTime = 72
                    for (let index = 0; index < 3; index++) {
                        projectile = sprites.createProjectileFromSprite(assets.image`pizza`, Player1Monke, -120, 0)
                    }
                }
            } else {
                if (BackAttack == 1) {
                    if (bTime == 0) {
                        bTime = 36
                        projectile = sprites.createProjectileFromSprite(assets.image`Speed Pizza`, Player1Monke, -240, 0)
                    }
                } else {
                    if (BackAttack == 0) {
                        if (bTime == 0) {
                            bTime = 72
                            projectile = sprites.createProjectileFromSprite(assets.image`Space Monke Projectile`, Player1Monke, -120, 0)
                        }
                    }
                }
            }
        }
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.BouncyOrange, function (sprite, otherSprite) {
    otherSprite.destroy()
    info.changeLifeBy(-1)
})
sprites.onCreated(SpriteKind.Boss, function (sprite) {
    sprite.setVelocity(-25, 0)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Attack == 4) {
        if (aTime == 0) {
            aTime = 36
            projectile = sprites.createProjectileFromSprite(assets.image`Space Monke Projectile`, Player1Monke, 60, 0)
            projectile = sprites.createProjectileFromSprite(assets.image`Space Monke Projectile`, Player1Monke, 60, 25)
            projectile = sprites.createProjectileFromSprite(assets.image`Space Monke Projectile`, Player1Monke, 60, -25)
        }
    } else {
        if (Attack == 3) {
            if (aTime == 0) {
                aTime = 36
                projectile = sprites.createProjectileFromSprite(img`
                    . . . . e . . . 
                    . . 4 e e e . . 
                    . 4 5 5 e e e . 
                    . 4 5 2 5 e e e 
                    4 5 5 5 5 5 e . 
                    5 5 5 5 2 5 4 . 
                    5 2 5 5 5 4 . . 
                    5 5 5 4 4 . . . 
                    `, Player1Monke, 60, 0)
            }
        } else {
            if (Attack == 2) {
                if (aTime == 0) {
                    aTime = 36
                    for (let index = 0; index < 3; index++) {
                        projectile = sprites.createProjectileFromSprite(assets.image`Big Pizza`, Player1Monke, 60, 0)
                    }
                }
            } else {
                if (Attack == 1) {
                    if (aTime == 0) {
                        aTime = 18
                        projectile = sprites.createProjectileFromSprite(assets.image`Speed Pizza`, Player1Monke, 120, 0)
                    }
                } else {
                    if (Attack == 0) {
                        if (aTime == 0) {
                            aTime = 36
                            projectile = sprites.createProjectileFromSprite(assets.image`Space Monke Projectile`, Player1Monke, 60, 0)
                        }
                    }
                }
            }
        }
    }
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.BouncyOrange, function (sprite, otherSprite) {
    otherSprite.destroy()
    sprite.destroy()
    info.changeScoreBy(2)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.PowerUp1, function (sprite, otherSprite) {
    otherSprite.destroy()
    controller.moveSprite(Player1Monke, 150, 150)
    pause(10000)
    controller.moveSprite(Player1Monke, 100, 100)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Boss, function (sprite, otherSprite) {
    Boss_Lives += 1
    if (Boss_Lives == 3) {
        otherSprite.destroy()
        info.changeScoreBy(4)
    }
    sprite.destroy()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.PowerUp3, function (sprite, otherSprite) {
    otherSprite.destroy()
    Attack = 1
    BackAttack = 1
    pause(10000)
    Attack = 0
    BackAttack = 0
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.PowerUp5, function (sprite, otherSprite) {
    otherSprite.destroy()
    Attack = 3
    BackAttack = 3
    pause(10000)
    Attack = 0
    BackAttack = 0
})
sprites.onCreated(SpriteKind.Enemy4, function (sprite) {
    sprite.setVelocity(-50, 0)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.HeatSeeker, function (sprite, otherSprite) {
    otherSprite.destroy()
    info.changeLifeBy(-1)
})
sprites.onCreated(SpriteKind.Enemy2, function (sprite) {
    sprite.setVelocity(-100, 0)
})
sprites.onOverlap(SpriteKind.BouncyOrange, SpriteKind.Shield, function (sprite, otherSprite) {
    sprite.destroy()
    info.changeScoreBy(2)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy4, function (sprite, otherSprite) {
    otherSprite.destroy()
    info.changeLifeBy(-1)
})
sprites.onOverlap(SpriteKind.HeatSeeker, SpriteKind.Shield, function (sprite, otherSprite) {
    sprite.destroy()
    info.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.HeatSeeker, function (sprite, otherSprite) {
    otherSprite.destroy()
    sprite.destroy()
    info.changeScoreBy(2)
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Shield, function (sprite, otherSprite) {
    sprite.destroy()
    info.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy2, function (sprite, otherSprite) {
    otherSprite.destroy()
    sprite.destroy()
    info.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.PowerUp4, function (sprite, otherSprite) {
    otherSprite.destroy()
    Attack = 2
    BackAttack = 2
    pause(10000)
    Attack = 0
    BackAttack = 0
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.PowerUp6, function (sprite, otherSprite) {
    otherSprite.destroy()
    Attack = 4
    BackAttack = 4
    pause(10000)
    Attack = 0
    BackAttack = 0
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.PowerUp7, function (sprite, otherSprite) {
    otherSprite.destroy()
    Shield = sprites.create(assets.image`Shield`, SpriteKind.Shield)
    Shield.follow(Player1Monke, 150)
    Player1Monke.setStayInScreen(true)
    pause(5000)
    Shield.destroy()
})
info.onLifeZero(function () {
    game.over(false)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy2, function (sprite, otherSprite) {
    otherSprite.destroy()
    info.changeLifeBy(-1)
})
sprites.onOverlap(SpriteKind.Enemy2, SpriteKind.Shield, function (sprite, otherSprite) {
    sprite.destroy()
    info.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    otherSprite.destroy()
    sprite.destroy()
    info.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    otherSprite.destroy()
    info.changeLifeBy(-1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Boss, function (sprite, otherSprite) {
    otherSprite.destroy()
    info.changeLifeBy(-1)
})
let Power_Up_7: Sprite = null
let Power_Up_6: Sprite = null
let Power_Up_5: Sprite = null
let Power_Up_4: Sprite = null
let Power_Up_3: Sprite = null
let Power_Up_2: Sprite = null
let Power_Up_1: Sprite = null
let enemySprite: Sprite = null
let speedSprite: Sprite = null
let mySprite3: Sprite = null
let richSprite: Sprite = null
let Bouncy_Orange: Sprite = null
let HeatSeeker: Sprite = null
let Shield: Sprite = null
let projectile: Sprite = null
let Boss_Lives = 0
let BackAttack = 0
let Attack = 0
let bTime = 0
let aTime = 0
let Player1Monke: Sprite = null
spriteutils.setLifeImage(assets.image`p1_life`)
scene.setBackgroundImage(assets.image`Space_BG`)
scene.setBackgroundColor(0)
Player1Monke = sprites.create(assets.image`space monke`, SpriteKind.Player)
controller.moveSprite(Player1Monke, 100, 100)
aTime = 0
bTime = 0
Player1Monke.setFlag(SpriteFlag.AutoDestroy, true)
Player1Monke.setStayInScreen(true)
Attack = 0
BackAttack = 0
Boss_Lives = 3
info.setLife(3)
game.onUpdateInterval(5000, function () {
    if (game.runtime() >= 35000 && game.runtime() <= 60000) {
        HeatSeeker = sprites.create(assets.image`Heat Seeker`, SpriteKind.HeatSeeker)
        HeatSeeker.setPosition(randint(125, 160), randint(0, 100))
        HeatSeeker.follow(Player1Monke, 100)
    }
})
game.onUpdateInterval(2000, function () {
    if (game.runtime() >= 110000) {
        HeatSeeker = sprites.create(assets.image`Heat Seeker`, SpriteKind.HeatSeeker)
        HeatSeeker.setPosition(randint(125, 160), randint(0, 100))
        HeatSeeker.follow(Player1Monke, 100)
    }
})
game.onUpdateInterval(1000, function () {
    if (randint(1, 15) == 15) {
        Bouncy_Orange = sprites.create(assets.image`Bouncy Orange`, SpriteKind.BouncyOrange)
        Bouncy_Orange.setPosition(randint(125, 160), randint(0, 100))
        Bouncy_Orange.setBounceOnWall(true)
    } else {
        if (randint(1, 45) == 45) {
            richSprite = sprites.create(assets.image`gapple`, SpriteKind.Enemy4)
            richSprite.setPosition(randint(125, 160), randint(0, 100))
        } else {
            if (randint(1, 15) == 15) {
                if (Boss_Lives == 3) {
                    mySprite3 = sprites.create(assets.image`Boss`, SpriteKind.Boss)
                    mySprite3.setPosition(randint(125, 160), randint(0, 100))
                    Boss_Lives = 0
                }
            } else {
                if (randint(1, 14) == 14) {
                    speedSprite = sprites.create(assets.image`Speed carrot`, SpriteKind.Enemy2)
                    speedSprite.setPosition(randint(125, 160), randint(0, 100))
                } else {
                    enemySprite = sprites.create(assets.image`broccoli`, SpriteKind.Enemy)
                    enemySprite.setPosition(randint(125, 160), randint(0, 100))
                }
            }
        }
    }
})
game.onUpdateInterval(1, function () {
    if (aTime > 0) {
        aTime = aTime - 1
    }
    if (bTime > 0) {
        bTime = bTime - 1
    }
})
game.onUpdateInterval(4000, function () {
    if (game.runtime() >= 64000 && game.runtime() <= 84000) {
        HeatSeeker = sprites.create(assets.image`Heat Seeker`, SpriteKind.HeatSeeker)
        HeatSeeker.setPosition(randint(125, 160), randint(0, 100))
        HeatSeeker.follow(Player1Monke, 100)
    }
})
forever(function () {
    music.playMelody("C5 B - A - B C5 - ", 250)
})
game.onUpdateInterval(6000, function () {
    if (game.runtime() >= 6000 && game.runtime() <= 30000) {
        HeatSeeker = sprites.create(assets.image`Heat Seeker`, SpriteKind.HeatSeeker)
        HeatSeeker.setPosition(randint(125, 160), randint(0, 100))
        HeatSeeker.follow(Player1Monke, 100)
    }
})
game.onUpdateInterval(3000, function () {
    if (game.runtime() >= 87000 && game.runtime() <= 108000) {
        HeatSeeker = sprites.create(assets.image`Heat Seeker`, SpriteKind.HeatSeeker)
        HeatSeeker.setPosition(randint(125, 160), randint(0, 100))
        HeatSeeker.follow(Player1Monke, 100)
    }
})
game.onUpdateInterval(20000, function () {
    if (game.runtime() > 20000) {
        if (Math.percentChance(14.29)) {
            Power_Up_1 = sprites.create(assets.image`Power Up 1`, SpriteKind.PowerUp1)
            Power_Up_1.setPosition(randint(10, 150), randint(10, 90))
        } else {
            if (Math.percentChance(16.6)) {
                Power_Up_2 = sprites.create(assets.image`Bad Power Up 1`, SpriteKind.PowerUp2)
                Power_Up_2.setPosition(randint(10, 150), randint(10, 90))
            } else {
                if (Math.percentChance(20)) {
                    Power_Up_3 = sprites.create(img`
                        .....77777777.....
                        ...77cccbbbbb77...
                        ..7ccb444444bbb7..
                        .7cc4444454444bc7.
                        .7e444444444544e7.
                        7eb454454444444bc7
                        7eb4444444444544e7
                        7ebb44444444444be7
                        .7eb4444454444be7.
                        787eeb444444bee687
                        7872eeeeeeeeee2787
                        7e6622222222226ce7
                        7ec67667776676cce7
                        7ebe88cc88ccc8ebe7
                        7eebecceeeeecebee7
                        .7eebb44444444ee7.
                        ..77ccccceeeee77..
                        ....7777777777....
                        `, SpriteKind.PowerUp3)
                    Power_Up_3.setPosition(randint(10, 150), randint(10, 90))
                } else {
                    if (Math.percentChance(25)) {
                        Power_Up_4 = sprites.create(assets.image`icecream`, SpriteKind.PowerUp4)
                        Power_Up_4.setPosition(randint(10, 150), randint(10, 90))
                    } else {
                        if (Math.percentChance(33.33)) {
                            Power_Up_5 = sprites.create(assets.image`lemon`, SpriteKind.PowerUp5)
                            Power_Up_5.setPosition(randint(10, 150), randint(10, 90))
                        } else {
                            if (Math.percentChance(50)) {
                                Power_Up_6 = sprites.create(assets.image`Power Up 6`, SpriteKind.PowerUp6)
                                Power_Up_6.setPosition(randint(10, 150), randint(10, 90))
                            } else {
                                Power_Up_7 = sprites.create(img`
                                    . . . . . . . 7 7 7 7 . . . . . 
                                    . . . . . 7 7 4 5 5 5 7 7 . . . 
                                    . . . . 7 4 5 6 2 2 7 6 6 7 . . 
                                    . . . 7 5 6 6 7 2 2 6 4 4 4 7 . 
                                    . . 7 5 2 2 7 6 6 4 5 5 5 5 7 . 
                                    . 7 5 6 2 2 8 8 5 5 5 5 5 4 5 7 
                                    . 7 5 6 7 7 8 5 4 5 4 5 5 5 5 7 
                                    7 4 5 8 6 6 5 5 5 5 5 5 4 5 5 7 
                                    7 5 c e 8 5 5 5 4 5 5 5 5 5 5 7 
                                    7 5 c c e 5 4 5 5 5 4 5 5 5 7 . 
                                    7 5 c c 5 5 5 5 5 5 5 5 4 7 . . 
                                    7 5 e c 5 4 5 4 5 5 5 7 7 . . . 
                                    7 5 e e 5 5 5 5 5 4 7 . . . . . 
                                    7 5 4 e 5 5 5 5 7 7 . . . . . . 
                                    . 7 5 4 5 5 4 7 . . . . . . . . 
                                    . . 7 7 7 7 7 . . . . . . . . . 
                                    `, SpriteKind.PowerUp7)
                                Power_Up_7.setPosition(randint(10, 150), randint(10, 90))
                            }
                        }
                    }
                }
            }
        }
    }
})
