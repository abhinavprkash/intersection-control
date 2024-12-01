from trafficSimulator import *

sim = Simulation()

n = 15
a = 2
b = 12
l = 500

# Nodes
WEST_RIGHT_START = (-b - l, a)
WEST_LEFT_START = (-b - l, -a)

WEST_RIGHT_START_2 = (-b - l, 3*a)
WEST_LEFT_START_2 = (-b - l, -a*3)

SOUTH_RIGHT_START = (a, b + l)
SOUTH_LEFT_START = (-a, b + l)

SOUTH_RIGHT_START_2 = (3*a, b + l)
SOUTH_LEFT_START_2 = (-a*3, b + l)

EAST_RIGHT_START = (b + l, -a)
EAST_LEFT_START = (b + l, a)

EAST_RIGHT_START_2 = (b + l, -a*3)
EAST_LEFT_START_2 = (b + l, a*3)

NORTH_RIGHT_START = (-a, -b - l)
NORTH_LEFT_START = (a, -b - l)

NORTH_RIGHT_START_2 = (-a*3, -b - l)
NORTH_LEFT_START_2 = (a*3, -b - l)

WEST_RIGHT = (-b, a)
WEST_LEFT = (-b, -a)

WEST_RIGHT_2 = (-b, a*3)
WEST_LEFT_2 = (-b, -a*3)

SOUTH_RIGHT = (a, b)
SOUTH_LEFT = (-a, b)

SOUTH_RIGHT_2 = (3*a, b)
SOUTH_LEFT_2 = (-a*3, b)

EAST_RIGHT = (b, -a)
EAST_LEFT = (b, a)

EAST_RIGHT_2 = (b, -a*3)
EAST_LEFT_2 = (b, a*3)

NORTH_RIGHT = (-a, -b)
NORTH_LEFT = (a, -b)

NORTH_RIGHT_2 = (-a*3, -b)
NORTH_LEFT_2 = (a*3, -b)

# Roads
WEST_INBOUND = (WEST_RIGHT_START, WEST_RIGHT)
WEST_INBOUND_2 = (WEST_RIGHT_START_2, WEST_RIGHT_2)

SOUTH_INBOUND = (SOUTH_RIGHT_START, SOUTH_RIGHT)
SOUTH_INBOUND_2 = (SOUTH_RIGHT_START_2, SOUTH_RIGHT_2)

EAST_INBOUND = (EAST_RIGHT_START, EAST_RIGHT)
EAST_INBOUND_2 = (EAST_RIGHT_START_2, EAST_RIGHT_2)

NORTH_INBOUND = (NORTH_RIGHT_START, NORTH_RIGHT)
NORTH_INBOUND_2 = (NORTH_RIGHT_START_2, NORTH_RIGHT_2)

WEST_OUTBOUND = (WEST_LEFT, WEST_LEFT_START)
WEST_OUTBOUND_2 = (WEST_LEFT_2, WEST_LEFT_START_2)

SOUTH_OUTBOUND = (SOUTH_LEFT, SOUTH_LEFT_START)
SOUTH_OUTBOUND_2 = (SOUTH_LEFT_2, SOUTH_LEFT_START_2)

EAST_OUTBOUND = (EAST_LEFT, EAST_LEFT_START)
EAST_OUTBOUND_2 = (EAST_LEFT_2, EAST_LEFT_START_2)

NORTH_OUTBOUND = (NORTH_LEFT, NORTH_LEFT_START)
NORTH_OUTBOUND_2 = (NORTH_LEFT_2, NORTH_LEFT_START_2)

WEST_STRAIGHT = (WEST_RIGHT, EAST_LEFT)
SOUTH_STRAIGHT = (SOUTH_RIGHT, NORTH_LEFT)
EAST_STRAIGHT = (EAST_RIGHT, WEST_LEFT)
NORTH_STRAIGHT = (NORTH_RIGHT, SOUTH_LEFT)

WEST_STRAIGHT_2 = (WEST_RIGHT_2, EAST_LEFT_2)
SOUTH_STRAIGHT_2 = (SOUTH_RIGHT_2, NORTH_LEFT_2)
EAST_STRAIGHT_2 = (EAST_RIGHT_2, WEST_LEFT_2)
NORTH_STRAIGHT_2 = (NORTH_RIGHT_2, SOUTH_LEFT_2)

WEST_RIGHT_TURN = turn_road(WEST_RIGHT, SOUTH_LEFT, TURN_RIGHT, n)
WEST_LEFT_TURN = turn_road(WEST_RIGHT, NORTH_LEFT, TURN_LEFT, n)

WEST_RIGHT_TURN_2 = turn_road(WEST_RIGHT_2, SOUTH_LEFT_2, TURN_RIGHT, n * 3)
WEST_LEFT_TURN_2 = turn_road(WEST_RIGHT_2, NORTH_LEFT_2, TURN_LEFT, n * 3)

SOUTH_RIGHT_TURN = turn_road(SOUTH_RIGHT, EAST_LEFT, TURN_RIGHT, n)
SOUTH_LEFT_TURN = turn_road(SOUTH_RIGHT, WEST_LEFT, TURN_LEFT, n)

SOUTH_RIGHT_TURN_2 = turn_road(SOUTH_RIGHT_2, EAST_LEFT_2, TURN_RIGHT, n * 3)
SOUTH_LEFT_TURN_2 = turn_road(SOUTH_RIGHT_2, WEST_LEFT_2, TURN_LEFT, n * 3)

EAST_RIGHT_TURN = turn_road(EAST_RIGHT, NORTH_LEFT, TURN_RIGHT, n)
EAST_LEFT_TURN = turn_road(EAST_RIGHT, SOUTH_LEFT, TURN_LEFT, n)

EAST_RIGHT_TURN_2 = turn_road(EAST_RIGHT_2, NORTH_LEFT_2, TURN_RIGHT, n * 3)
EAST_LEFT_TURN_2 = turn_road(EAST_RIGHT_2, SOUTH_LEFT_2, TURN_LEFT, n * 3)

NORTH_RIGHT_TURN = turn_road(NORTH_RIGHT, WEST_LEFT, TURN_RIGHT, n)
NORTH_LEFT_TURN = turn_road(NORTH_RIGHT, EAST_LEFT, TURN_LEFT, n)

NORTH_RIGHT_TURN_2 = turn_road(NORTH_RIGHT_2, WEST_LEFT_2, TURN_RIGHT, n * 3)
NORTH_LEFT_TURN_2 = turn_road(NORTH_RIGHT_2, EAST_LEFT_2, TURN_LEFT, n * 3)

sim.create_roads([
    WEST_INBOUND, #0
    SOUTH_INBOUND, #1
    EAST_INBOUND,
    NORTH_INBOUND, #3

    WEST_OUTBOUND, 
    SOUTH_OUTBOUND,
    EAST_OUTBOUND, # 6
    NORTH_OUTBOUND, #7

    WEST_INBOUND_2,
    SOUTH_INBOUND_2,
    EAST_INBOUND_2,
    NORTH_INBOUND_2, #11

    WEST_OUTBOUND_2,
    SOUTH_OUTBOUND_2,
    EAST_OUTBOUND_2,
    NORTH_OUTBOUND_2, #15

    WEST_STRAIGHT,
    SOUTH_STRAIGHT,
    EAST_STRAIGHT,
    NORTH_STRAIGHT, #19

    WEST_STRAIGHT_2,
    SOUTH_STRAIGHT_2,
    EAST_STRAIGHT_2,
    NORTH_STRAIGHT_2, #23

    *WEST_RIGHT_TURN,
    *WEST_LEFT_TURN, #25

    *SOUTH_RIGHT_TURN,
    *SOUTH_LEFT_TURN, #27

    *EAST_RIGHT_TURN,
    *EAST_LEFT_TURN, #29

    *NORTH_RIGHT_TURN,
    *NORTH_LEFT_TURN, #31

    *WEST_RIGHT_TURN_2,
    *WEST_LEFT_TURN_2, #33

    *SOUTH_RIGHT_TURN_2,
    *SOUTH_LEFT_TURN_2, #35

    *EAST_RIGHT_TURN_2,
    *EAST_LEFT_TURN_2, #37

    *NORTH_RIGHT_TURN_2,
    *NORTH_LEFT_TURN_2, #39

    
])


def road(a):
    return range(a, a + n)


# Traffic distribution
sim.create_gen({
    'vehicle_rate': 30,
    'vehicles': [
        [3, {'path': [0, 8 + 8, 6]}],
        [1, {'path': [0, *road(12 + 12), 5]}],
        [1, {'path': [0, *road(12 + n + 12), 7]}],

        [1, {'path': [1, 9 + 8, 7]}],
        [0, {'path': [1, *road(12 + 2 * n + 12), 6]}],
        [1, {'path': [1, *road(12 + 3 * n + 12), 4]}],

        [3, {'path': [2, 10 + 8, 4]}],
        [1, {'path': [2, *road(12 + 4 * n + 12), 7]}],
        [1, {'path': [2, *road(12 + 5 * n + 12), 5]}],

        [1, {'path': [3, 11 + 8, 5]}],
        [0, {'path': [3, *road(12 + 6 * n + 12), 4]}],
        [1, {'path': [3, *road(12 + 7 * n + 12), 6]}],

        [3, {'path': [0 + 8, 8 + 8 + 4, 6 + 8]}],
        [1, {'path': [0 + 8, *road(12 + 8 * n + 12 + 8), 5 + 8]}],
        # [1, {'path': [0 + 8, *road(12 + 9 * n + 12 + 8), 7 + 8]}],

        [1, {'path': [1 + 8, 9 + 8 + 4, 7 + 8]}],
        # [1, {'path': [1 + 8, *road(12 + 10 * n + 12 + 8), 6 + 8]}],
        # [1, {'path': [1 + 8, *road(12 + 3 * n + 12), 4 + 8]}],

        [3, {'path': [2 + 8, 10 + 8 + 4, 4 + 8]}],
        # [1, {'path': [2 + 8, *road(12 + 12 * n + 12 + 8), 7 + 8]}],
        # [1, {'path': [2 + 8, *road(12 + 5 * n + 12), 5 + 8]}],

        [1, {'path': [3 + 8, 11 + 8 + 4, 5 + 8]}],
        # [1, {'path': [3 + 8, *road(12 + 14 * n + 12 + 8), 4 + 8]}],
        # [1, {'path': [3 + 8, *road(12 + 7 * n + 12), 6 + 8]}]
    ]})

sim.create_signal([[1, 3, 9, 11],  [0, 2, 8, 10]])

# Start simulation
win = Window(sim)
win.zoom = 5
win.run(steps_per_update=3)