from enum import Enum


class CardinalPoint(Enum):
    NORTH = 0
    NORTH_NORTHEAST = 22
    NORTHEAST = 45
    EAST_NORTHEAST = 67
    EAST = 90
    EAST_SOUTHEAST = 112
    SOUTHEAST = 135
    SOUTH_SOUTHEAST = 157
    SOUTH = 180
    SOUTH_SOUTHWEST = 202
    SOUTHWEST = 225
    WEST_SOUTHWEST = 247
    WEST = 270
    WEST_NORTHWEST = 292
    NORTHWEST = 315
    NORTH_NORTHWEST = 337


class CardinalPointAbbreviation(Enum):
    N = CardinalPoint.NORTH
    NNE = CardinalPoint.NORTH_NORTHEAST
    NE = CardinalPoint.NORTHEAST
    ENE = CardinalPoint.EAST_NORTHEAST
    E = CardinalPoint.EAST
    ESE = CardinalPoint.EAST_SOUTHEAST
    SE = CardinalPoint.SOUTHEAST
    SSE = CardinalPoint.SOUTH_SOUTHEAST
    S = CardinalPoint.SOUTH
    SSW = CardinalPoint.SOUTH_SOUTHWEST
    SW = CardinalPoint.SOUTHWEST
    WSW = CardinalPoint.WEST_SOUTHWEST
    W = CardinalPoint.WEST
    WNW = CardinalPoint.WEST_NORTHWEST
    NW = CardinalPoint.NORTHWEST
    NNW = CardinalPoint.NORTH_NORTHWEST
