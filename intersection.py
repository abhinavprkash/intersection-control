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

WEST_RIGHT_START_3 = (-b - l, 5*a)
WEST_LEFT_START_3 = (-b - l, -a*5)

SOUTH_RIGHT_START = (a, b + l)
SOUTH_LEFT_START = (-a, b + l)

SOUTH_RIGHT_START_2 = (3*a, b + l)
SOUTH_LEFT_START_2 = (-a*3, b + l)

SOUTH_RIGHT_START_3 = (5*a, b + l)
SOUTH_LEFT_START_3 = (-a*5, b + l)

EAST_RIGHT_START = (b + l, -a)
EAST_LEFT_START = (b + l, a)

EAST_RIGHT_START_2 = (b + l, -a*3)
EAST_LEFT_START_2 = (b + l, a*3)

EAST_RIGHT_START_3 = (b + l, -a*5)
EAST_LEFT_START_3 = (b + l, a*5)

NORTH_RIGHT_START = (-a, -b - l)
NORTH_LEFT_START = (a, -b - l)

NORTH_RIGHT_START_2 = (-a*3, -b - l)
NORTH_LEFT_START_2 = (a*3, -b - l)

NORTH_RIGHT_START_3 = (-a*5, -b - l)
NORTH_LEFT_START_3 = (a*5, -b - l)

WEST_RIGHT = (-b, a)
WEST_LEFT = (-b, -a)

WEST_RIGHT_2 = (-b, a*3)
WEST_LEFT_2 = (-b, -a*3)

WEST_RIGHT_3 = (-b, a*5)
WEST_LEFT_3 = (-b, -a*5)

SOUTH_RIGHT = (a, b)
SOUTH_LEFT = (-a, b)

SOUTH_RIGHT_2 = (3*a, b)
SOUTH_LEFT_2 = (-a*3, b)

SOUTH_RIGHT_3 = (5*a, b)
SOUTH_LEFT_3 = (-a*5, b)

EAST_RIGHT = (b, -a)
EAST_LEFT = (b, a)

EAST_RIGHT_2 = (b, -a*3)
EAST_LEFT_2 = (b, a*3)

EAST_RIGHT_3 = (b, -a*5)
EAST_LEFT_3 = (b, a*5)

NORTH_RIGHT = (-a, -b)
NORTH_LEFT = (a, -b)

NORTH_RIGHT_2 = (-a*3, -b)
NORTH_LEFT_2 = (a*3, -b)

NORTH_RIGHT_3 = (-a*5, -b)
NORTH_LEFT_3 = (a*5, -b)

# Roads
WEST_INBOUND = (WEST_RIGHT_START, WEST_RIGHT)
WEST_INBOUND_2 = (WEST_RIGHT_START_2, WEST_RIGHT_2)
WEST_INBOUND_3 = (WEST_RIGHT_START_3, WEST_RIGHT_3)

SOUTH_INBOUND = (SOUTH_RIGHT_START, SOUTH_RIGHT)
SOUTH_INBOUND_2 = (SOUTH_RIGHT_START_2, SOUTH_RIGHT_2)
SOUTH_INBOUND_3 = (SOUTH_RIGHT_START_3, SOUTH_RIGHT_3)

EAST_INBOUND = (EAST_RIGHT_START, EAST_RIGHT)
EAST_INBOUND_2 = (EAST_RIGHT_START_2, EAST_RIGHT_2)
EAST_INBOUND_3 = (EAST_RIGHT_START_3, EAST_RIGHT_3)

NORTH_INBOUND = (NORTH_RIGHT_START, NORTH_RIGHT)
NORTH_INBOUND_2 = (NORTH_RIGHT_START_2, NORTH_RIGHT_2)
NORTH_INBOUND_3 = (NORTH_RIGHT_START_3, NORTH_RIGHT_3)

WEST_OUTBOUND = (WEST_LEFT, WEST_LEFT_START)
WEST_OUTBOUND_2 = (WEST_LEFT_2, WEST_LEFT_START_2)
WEST_OUTBOUND_3 = (WEST_LEFT_3, WEST_LEFT_START_3)

SOUTH_OUTBOUND = (SOUTH_LEFT, SOUTH_LEFT_START)
SOUTH_OUTBOUND_2 = (SOUTH_LEFT_2, SOUTH_LEFT_START_2)
SOUTH_OUTBOUND_3 = (SOUTH_LEFT_3, SOUTH_LEFT_START_3)

EAST_OUTBOUND = (EAST_LEFT, EAST_LEFT_START)
EAST_OUTBOUND_2 = (EAST_LEFT_2, EAST_LEFT_START_2)
EAST_OUTBOUND_3 = (EAST_LEFT_3, EAST_LEFT_START_3)

NORTH_OUTBOUND = (NORTH_LEFT, NORTH_LEFT_START)
NORTH_OUTBOUND_2 = (NORTH_LEFT_2, NORTH_LEFT_START_2)
NORTH_OUTBOUND_3 = (NORTH_LEFT_3, NORTH_LEFT_START_3)

WEST_STRAIGHT = (WEST_RIGHT, EAST_LEFT)
SOUTH_STRAIGHT = (SOUTH_RIGHT, NORTH_LEFT)
EAST_STRAIGHT = (EAST_RIGHT, WEST_LEFT)
NORTH_STRAIGHT = (NORTH_RIGHT, SOUTH_LEFT)

WEST_STRAIGHT_2 = (WEST_RIGHT_2, EAST_LEFT_2)
SOUTH_STRAIGHT_2 = (SOUTH_RIGHT_2, NORTH_LEFT_2)
EAST_STRAIGHT_2 = (EAST_RIGHT_2, WEST_LEFT_2)
NORTH_STRAIGHT_2 = (NORTH_RIGHT_2, SOUTH_LEFT_2)

WEST_STRAIGHT_3 = (WEST_RIGHT_3, EAST_LEFT_3)
SOUTH_STRAIGHT_3 = (SOUTH_RIGHT_3, NORTH_LEFT_3)
EAST_STRAIGHT_3 = (EAST_RIGHT_3, WEST_LEFT_3)
NORTH_STRAIGHT_3 = (NORTH_RIGHT_3, SOUTH_LEFT_3)

WEST_RIGHT_TURN = turn_road(WEST_RIGHT, SOUTH_LEFT, TURN_RIGHT, n)
WEST_LEFT_TURN = turn_road(WEST_RIGHT, NORTH_LEFT, TURN_LEFT, n)

SOUTH_RIGHT_TURN = turn_road(SOUTH_RIGHT, EAST_LEFT, TURN_RIGHT, n)
SOUTH_LEFT_TURN = turn_road(SOUTH_RIGHT, WEST_LEFT, TURN_LEFT, n)

EAST_RIGHT_TURN = turn_road(EAST_RIGHT, NORTH_LEFT, TURN_RIGHT, n)
EAST_LEFT_TURN = turn_road(EAST_RIGHT, SOUTH_LEFT, TURN_LEFT, n)

NORTH_RIGHT_TURN = turn_road(NORTH_RIGHT, WEST_LEFT, TURN_RIGHT, n)
NORTH_LEFT_TURN = turn_road(NORTH_RIGHT, EAST_LEFT, TURN_LEFT, n)

WEST_RIGHT_TURN_2 = turn_road(WEST_RIGHT_2, SOUTH_LEFT_2, TURN_RIGHT, n )
WEST_LEFT_TURN_2 = turn_road(WEST_RIGHT_2, NORTH_LEFT_2, TURN_LEFT, n)

SOUTH_RIGHT_TURN_2 = turn_road(SOUTH_RIGHT_2, EAST_LEFT_2, TURN_RIGHT, n)
SOUTH_LEFT_TURN_2 = turn_road(SOUTH_RIGHT_2, WEST_LEFT_2, TURN_LEFT, n)

EAST_RIGHT_TURN_2 = turn_road(EAST_RIGHT_2, NORTH_LEFT_2, TURN_RIGHT, n)
EAST_LEFT_TURN_2 = turn_road(EAST_RIGHT_2, SOUTH_LEFT_2, TURN_LEFT, n)

NORTH_RIGHT_TURN_2 = turn_road(NORTH_RIGHT_2, WEST_LEFT_2, TURN_RIGHT, n)
NORTH_LEFT_TURN_2 = turn_road(NORTH_RIGHT_2, EAST_LEFT_2, TURN_LEFT, n )

WEST_RIGHT_TURN_3 = turn_road(WEST_RIGHT_3, SOUTH_LEFT_3, TURN_RIGHT, n)
WEST_LEFT_TURN_3 = turn_road(WEST_RIGHT_3, NORTH_LEFT_3, TURN_LEFT, n )

SOUTH_RIGHT_TURN_3 = turn_road(SOUTH_RIGHT_3, EAST_LEFT_3, TURN_RIGHT, n)
SOUTH_LEFT_TURN_3 = turn_road(SOUTH_RIGHT_3, WEST_LEFT_3, TURN_LEFT, n )


EAST_RIGHT_TURN_3 = turn_road(EAST_RIGHT_3, NORTH_LEFT_3, TURN_RIGHT, n)
EAST_LEFT_TURN_3 = turn_road(EAST_RIGHT_3, SOUTH_LEFT_3, TURN_LEFT, n )


NORTH_RIGHT_TURN_3 = turn_road(NORTH_RIGHT_3, WEST_LEFT_3, TURN_RIGHT, n)
NORTH_LEFT_TURN_3 = turn_road(NORTH_RIGHT_3, EAST_LEFT_3, TURN_LEFT, n )

sim.create_roads([
    WEST_INBOUND, #0
    SOUTH_INBOUND, #1
    EAST_INBOUND, #2
    NORTH_INBOUND, #3

    WEST_OUTBOUND,  #4
    SOUTH_OUTBOUND, #5
    EAST_OUTBOUND, # 6
    NORTH_OUTBOUND, #7

    WEST_INBOUND_2, #8
    SOUTH_INBOUND_2, #9
    EAST_INBOUND_2, #10
    NORTH_INBOUND_2, #11

    WEST_OUTBOUND_2, #12
    SOUTH_OUTBOUND_2, #13
    EAST_OUTBOUND_2, #14
    NORTH_OUTBOUND_2, #15
    
    WEST_INBOUND_3,
    SOUTH_INBOUND_3,
    EAST_INBOUND_3,
    NORTH_INBOUND_3, 

    WEST_OUTBOUND_3,
    SOUTH_OUTBOUND_3,
    EAST_OUTBOUND_3,
    NORTH_OUTBOUND_3, 

    WEST_STRAIGHT,  #16
    SOUTH_STRAIGHT, #17
    EAST_STRAIGHT, #18
    NORTH_STRAIGHT, #19

    WEST_STRAIGHT_2, #20
    SOUTH_STRAIGHT_2, #21
    EAST_STRAIGHT_2, #22
    NORTH_STRAIGHT_2, #23

    WEST_STRAIGHT_3, 
    SOUTH_STRAIGHT_3, 
    EAST_STRAIGHT_3, 
    NORTH_STRAIGHT_3, 

    *WEST_RIGHT_TURN, #24
    *WEST_LEFT_TURN, #25

    *SOUTH_RIGHT_TURN,  #26
    *SOUTH_LEFT_TURN, #27

    *EAST_RIGHT_TURN, #28
    *EAST_LEFT_TURN, #29

    *NORTH_RIGHT_TURN, #30
    *NORTH_LEFT_TURN, #31

    *WEST_RIGHT_TURN_2, #32
    *WEST_LEFT_TURN_2, #33

    *SOUTH_RIGHT_TURN_2, #34
    *SOUTH_LEFT_TURN_2, #35

    *EAST_RIGHT_TURN_2, #35
    *EAST_LEFT_TURN_2, #37

    *NORTH_RIGHT_TURN_2, #38
    *NORTH_LEFT_TURN_2, #39

    *WEST_RIGHT_TURN_3,
    *WEST_LEFT_TURN_3, 

    *SOUTH_RIGHT_TURN_3,
    *SOUTH_LEFT_TURN_3, 

    *EAST_RIGHT_TURN_3,
    *EAST_LEFT_TURN_3, 

    *NORTH_RIGHT_TURN_3,
    *NORTH_LEFT_TURN_3, 
])


def road(a):
    return range(a, a + n)


# Traffic distribution
sim.create_gen({
    'vehicle_rate': 60,
    'vehicles': [
        # left most lanes
        # [3, {'path': [0, 16 + 8, 6]}],
        # [1, {'path': [0, *road(36), 5]}],
        [1, {'path': [0, *road(36 + n), 7]}],

        # [1, {'path': [1, 17 + 8, 7]}],
        # [0, {'path': [1, *road(36 + 2 * n), 6]}],
        [1, {'path': [1, *road(36 + 3 * n), 4]}],

        # [3, {'path': [2, 18 + 8, 4]}],
        # [1, {'path': [2, *road(36 + 4 * n ), 7]}],
        [1, {'path': [2, *road(36 + 5 * n), 5]}],

        # [1, {'path': [3, 19 + 8, 5]}],
        # [0, {'path': [3, *road(36 + 6 * n ), 4]}],
        [1, {'path': [3, *road(36 + 7 * n), 6]}],

        # middle lanes
        [3, {'path': [8, 20 + 8, 14]}],
        # [1, {'path': [8, *road(36 + 8 * n), 13]}],
        # [1, {'path': [8, *road(36 + 9 * n), 15]}],

        [1, {'path': [9, 21 + 8, 15]}],
        # [1, {'path': [9, *road(36 + 10 * n), 14]}],
        # [1, {'path': [9, *road(36 + 11 * n), 12]}],

        [3, {'path': [10, 22 + 8, 12]}],
        # [1, {'path': [10, *road(36 + 12 * n), 15]}],
        # [1, {'path': [10, *road(36 + 13 * n), 13]}],

        [1, {'path': [11, 23 + 8, 13]}],
        # [1, {'path': [11, *road(36 + 14 * n), 12]}],
        # [1, {'path': [11, *road(36 + 15 * n), 14]}],

        # right lanes
        [3, {'path': [16, 24 + 8, 22]}],
        [1, {'path': [16, *road(36 + 16 * n), 21]}],
        # [1, {'path': [16, *road(36 + 17 * n), 23]}],

        [1, {'path': [17, 25 + 8, 23]}],
        [1, {'path': [17, *road(36 + 18 * n), 22]}],
        # [1, {'path': [17, *road(36 + 19 * n), 20]}],

        [3, {'path': [18, 26 + 8, 20]}],
        [1, {'path': [18, *road(36 + 20 * n), 23]}],
        # [1, {'path': [18, *road(36 + 21 * n), 21]}],

        [1, {'path': [19, 27 + 8, 21]}],
        [1, {'path': [19, *road(36 + 22 * n), 20]}],
        # [1, {'path': [19, *road(36 + 23 * n), 22]}]
    ]})

sim.create_signal([[1, 3, 9, 11, 17, 19], [0, 2, 8, 10, 16, 18]])

# Start simulation
win = Window(sim)
win.zoom = 5
win.run(steps_per_update=6)