from enum import Enum


class Action(Enum):
    IDLE = 0
    WALK = 1
    WAVE = 2
    BRUSH_HAIR = 3
    CATCH = 4
    CLAP = 5
    CLIMB_STAIRS = 6
    GOLF = 7
    JUMP = 8
    KICK_BALL = 9
    PICK = 10
    POUR = 11
    PULLUP = 12
    PUSH = 13
    RUN = 14
    SHOOT_BALL = 15
    SHOOT_BOW = 16
    SHOOT_GUN = 17
    SIT = 18
    STAND = 19
    SWING_BASEBALL = 20
    THROW = 21

jhmdb_actions = [
    Action.BRUSH_HAIR,
    Action.CATCH,
    Action.CLAP,
    Action.CLIMB_STAIRS,
    Action.GOLF,
    Action.JUMP,
    Action.KICK_BALL,
    Action.PICK,
    Action.POUR,
    Action.PULLUP,
    Action.PUSH,
    Action.RUN,
    Action.SHOOT_BALL,
    Action.SHOOT_BOW,
    Action.SHOOT_GUN,
    Action.SIT,
    Action.STAND,
    Action.SWING_BASEBALL,
    Action.THROW,
    Action.WALK,
    Action.WAVE
]

ofp_actions = [
    Action.IDLE,
    Action.WALK,
    Action.WAVE
]