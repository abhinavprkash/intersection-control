from trafficSimulator import *

sim = Simulation()

a = 1.85  # Half lane width
b = 12    # Offset from the center of the intersection
l = 500   # Length of incoming/outgoing roads

# Define lane offsets for four lanes
lane_offsets = [3*a, a, -a, -3*a]

roads = []

# Function to create inbound and outbound lanes for a side
def create_side_roads(side, b, l, lane_offsets, roads):
    INBOUND_LANE_INDICES = []
    OUTBOUND_LANE_INDICES = []

    for lane_pos in lane_offsets:
        if side == 'WEST':
            inbound_start = (-b - l, lane_pos)
            inbound_end = (-b, lane_pos)
            outbound_start = (-b, lane_pos)
            outbound_end = (-b - l, lane_pos)
        elif side == 'SOUTH':
            inbound_start = (lane_pos, b + l)
            inbound_end = (lane_pos, b)
            outbound_start = (lane_pos, b)
            outbound_end = (lane_pos, b + l)
        elif side == 'EAST':
            inbound_start = (b + l, -lane_pos)
            inbound_end = (b, -lane_pos)
            outbound_start = (b, -lane_pos)
            outbound_end = (b + l, -lane_pos)
        elif side == 'NORTH':
            inbound_start = (-lane_pos, -b - l)
            inbound_end = (-lane_pos, -b)
            outbound_start = (-lane_pos, -b)
            outbound_end = (-lane_pos, -b - l)
        else:
            raise ValueError('Invalid side')

        roads.append((inbound_start, inbound_end))
        INBOUND_LANE_INDICES.append(len(roads) - 1)

        roads.append((outbound_start, outbound_end))
        OUTBOUND_LANE_INDICES.append(len(roads) - 1)

    return INBOUND_LANE_INDICES, OUTBOUND_LANE_INDICES

# Create roads for all sides
WEST_INBOUND_LANE_INDICES, WEST_OUTBOUND_LANE_INDICES = create_side_roads('WEST', b, l, lane_offsets, roads)
SOUTH_INBOUND_LANE_INDICES, SOUTH_OUTBOUND_LANE_INDICES = create_side_roads('SOUTH', b, l, lane_offsets, roads)
EAST_INBOUND_LANE_INDICES, EAST_OUTBOUND_LANE_INDICES = create_side_roads('EAST', b, l, lane_offsets, roads)
NORTH_INBOUND_LANE_INDICES, NORTH_OUTBOUND_LANE_INDICES = create_side_roads('NORTH', b, l, lane_offsets, roads)

# Create straight roads through the intersection
for i in range(4):
    # West to East
    start = roads[WEST_INBOUND_LANE_INDICES[i]][1]
    end = roads[EAST_OUTBOUND_LANE_INDICES[i]][0]
    roads.append((start, end))

    # South to North
    start = roads[SOUTH_INBOUND_LANE_INDICES[i]][1]
    end = roads[NORTH_OUTBOUND_LANE_INDICES[i]][0]
    roads.append((start, end))

    # East to West
    start = roads[EAST_INBOUND_LANE_INDICES[i]][1]
    end = roads[WEST_OUTBOUND_LANE_INDICES[i]][0]
    roads.append((start, end))

    # North to South
    start = roads[NORTH_INBOUND_LANE_INDICES[i]][1]
    end = roads[SOUTH_OUTBOUND_LANE_INDICES[i]][0]
    roads.append((start, end))

# Create right turn roads
# Create right turn roads
def create_right_turn(start_lane_indices, end_lane_indices, turn_direction):
    turn_roads = []
    for i in range(4):
        start = roads[start_lane_indices[i]][1]
        end = roads[end_lane_indices[i]][0]
        # Corrected keyword argument
        turn_road_points = turn_road(start, end, turn_direction, resolution=15)
        turn_roads.extend(turn_road_points)
    return turn_roads


# Define TURN_LEFT and TURN_RIGHT constants
TURN_LEFT = 0
TURN_RIGHT = 1

# Create turning roads for all directions
turn_roads = []

# West Right Turn to South
turn_roads.extend(create_right_turn(WEST_INBOUND_LANE_INDICES, SOUTH_OUTBOUND_LANE_INDICES, TURN_RIGHT))

# South Right Turn to East
turn_roads.extend(create_right_turn(SOUTH_INBOUND_LANE_INDICES, EAST_OUTBOUND_LANE_INDICES, TURN_RIGHT))

# East Right Turn to North
turn_roads.extend(create_right_turn(EAST_INBOUND_LANE_INDICES, NORTH_OUTBOUND_LANE_INDICES, TURN_RIGHT))

# North Right Turn to West
turn_roads.extend(create_right_turn(NORTH_INBOUND_LANE_INDICES, WEST_OUTBOUND_LANE_INDICES, TURN_RIGHT))

# Add all roads to the simulation
sim.create_roads(roads + turn_roads)

# Vehicle generation logic
# Vehicle generation logic
sim.create_gen({
    'vehicle_rate': 30,
    'vehicles': [
        # West to East, West to North (Leftmost lanes handle left or straight)
        [3, {'path': [WEST_INBOUND_LANE_INDICES[0], len(roads) - 8, EAST_OUTBOUND_LANE_INDICES[0]]}],  # Straight
        [3, {'path': [WEST_INBOUND_LANE_INDICES[0], *turn_roads[:15]]}],  # Left turn to North
        [3, {'path': [WEST_INBOUND_LANE_INDICES[1], len(roads) - 8, EAST_OUTBOUND_LANE_INDICES[1]]}],  # Straight

        # West to East, West to South (Rightmost lanes handle right or straight)
        [3, {'path': [WEST_INBOUND_LANE_INDICES[2], len(roads) - 8, EAST_OUTBOUND_LANE_INDICES[2]]}],  # Straight
        [3, {'path': [WEST_INBOUND_LANE_INDICES[3], *turn_roads[15:30]]}],  # Right turn to South

        # South to North, South to West (Leftmost lanes handle left or straight)
        [3, {'path': [SOUTH_INBOUND_LANE_INDICES[0], len(roads) - 7, NORTH_OUTBOUND_LANE_INDICES[0]]}],  # Straight
        [3, {'path': [SOUTH_INBOUND_LANE_INDICES[0], *turn_roads[30:45]]}],  # Left turn to West
        [3, {'path': [SOUTH_INBOUND_LANE_INDICES[1], len(roads) - 7, NORTH_OUTBOUND_LANE_INDICES[1]]}],  # Straight

        # South to North, South to East (Rightmost lanes handle right or straight)
        [3, {'path': [SOUTH_INBOUND_LANE_INDICES[2], len(roads) - 7, NORTH_OUTBOUND_LANE_INDICES[2]]}],  # Straight
        [3, {'path': [SOUTH_INBOUND_LANE_INDICES[3], *turn_roads[45:60]]}],  # Right turn to East

        # East to West, East to South (Leftmost lanes handle left or straight)
        [3, {'path': [EAST_INBOUND_LANE_INDICES[0], len(roads) - 6, WEST_OUTBOUND_LANE_INDICES[0]]}],  # Straight
        [3, {'path': [EAST_INBOUND_LANE_INDICES[0], *turn_roads[60:75]]}],  # Left turn to South
        [3, {'path': [EAST_INBOUND_LANE_INDICES[1], len(roads) - 6, WEST_OUTBOUND_LANE_INDICES[1]]}],  # Straight

        # East to West, East to North (Rightmost lanes handle right or straight)
        [3, {'path': [EAST_INBOUND_LANE_INDICES[2], len(roads) - 6, WEST_OUTBOUND_LANE_INDICES[2]]}],  # Straight
        [3, {'path': [EAST_INBOUND_LANE_INDICES[3], *turn_roads[75:90]]}],  # Right turn to North

        # North to South, North to East (Leftmost lanes handle left or straight)
        [3, {'path': [NORTH_INBOUND_LANE_INDICES[0], len(roads) - 5, SOUTH_OUTBOUND_LANE_INDICES[0]]}],  # Straight
        [3, {'path': [NORTH_INBOUND_LANE_INDICES[0], *turn_roads[90:105]]}],  # Left turn to East
        [3, {'path': [NORTH_INBOUND_LANE_INDICES[1], len(roads) - 5, SOUTH_OUTBOUND_LANE_INDICES[1]]}],  # Straight

        # North to South, North to West (Rightmost lanes handle right or straight)
        [3, {'path': [NORTH_INBOUND_LANE_INDICES[2], len(roads) - 5, SOUTH_OUTBOUND_LANE_INDICES[2]]}],  # Straight
        [3, {'path': [NORTH_INBOUND_LANE_INDICES[3], *turn_roads[105:120]]}],  # Right turn to West
    ]
})


# Traffic signal controlling all inbound lanes
sim.create_signal([
    WEST_INBOUND_LANE_INDICES + SOUTH_INBOUND_LANE_INDICES,
    EAST_INBOUND_LANE_INDICES + NORTH_INBOUND_LANE_INDICES
])

# Start simulation
win = Window(sim)
win.zoom = 5
win.run(steps_per_update=10)
