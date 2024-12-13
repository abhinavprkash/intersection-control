class TrafficSignal:
    def __init__(self, roads, config={}):
        # Initialize roads
        self.roads = roads
        # Set default configuration
        self.set_default_config()
        # Update configuration
        for attr, val in config.items():
            setattr(self, attr, val)
        # Calculate properties
        self.init_properties()
        self.traffic_data = [
            [0, 0, 0, 0, 0, 0],  # Person, Bicycle, Car, Motorbike, Bus, Truck
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
        self.vehicles_passed = 0

    def set_default_config(self):
        self.cycle = [
            (True, False, False, False),  # Phase 0
            (False, True, False, False),  # Phase 1
            (False, False, True, False),  # Phase 2
            (False, False, False, True)   # Phase 3
        ]
        self.fixed_flag = True
        self.adjust_flag = False
        self.cycle_length_1 = 30
        self.cycle_length_2 = 30
        self.cycle_length_3 = 30  # Added length for the new phase
        self.cycle_length_4 = 30  # New phase (4th)
        self.slow_distance = 50
        self.slow_factor = 0.4
        self.stop_distance = 15
        self.current_cycle_index = 0
        self.time_off = 0

        self.time_steps_passed = 0
        self.new_cycle_index = -1

    def init_properties(self):
        for i in range(len(self.roads)):
            for road in self.roads[i]:
                road.set_traffic_signal(self, i)

    @property
    def current_cycle(self):
        return self.cycle[self.current_cycle_index]

    def update(self, sim):
        temp = sim.t - self.time_off
        if self.fixed_flag:
            if temp > self.cycle_length_1 and self.current_cycle_index == 0:
                self.time_off = sim.t
                self.current_cycle_index = 1
                temp = 0
                return
            if temp > self.cycle_length_2 and self.current_cycle_index == 1:
                self.time_off = sim.t
                self.current_cycle_index = 2
                temp = 0
                return
            if temp > self.cycle_length_3 and self.current_cycle_index == 2:
                self.time_off = sim.t
                self.current_cycle_index = 3
                temp = 0
                return
            if temp > self.cycle_length_4 and self.current_cycle_index == 3:
                self.time_off = sim.t
                self.current_cycle_index = 0
                temp = 0

        if not self.fixed_flag:
            if self.current_cycle_index in (2, 3):
                if self.time_steps_passed != 200:
                    self.time_steps_passed += 1
                else:
                    self.current_cycle_index = self.new_cycle_index
                    self.time_steps_passed = 0
                    self.new_cycle_index = -1

            if temp > self.cycle_length_1 and self.current_cycle_index == 0:
                self.adjust_green_phase(sim, 1, 3)  # Adjust for Phase 1
                self.time_off = sim.t
                self.new_cycle_index = 1
                self.current_cycle_index = 2
                temp = 0
                return

            if temp > self.cycle_length_2 and self.current_cycle_index == 1:
                self.adjust_green_phase(sim, 2, 4)  # Adjust for Phase 2
                self.time_off = sim.t
                self.new_cycle_index = 2
                self.current_cycle_index = 3
                temp = 0
                return

            if temp > self.cycle_length_3 and self.current_cycle_index == 2:
                self.adjust_green_phase(sim, 3, 0)  # Adjust for Phase 3
                self.time_off = sim.t
                self.new_cycle_index = 3
                self.current_cycle_index = 0
                temp = 0
                return

            if temp > self.cycle_length_4 and self.current_cycle_index == 3:
                self.adjust_green_phase(sim, 4, 1)  # Adjust for Phase 4
                self.time_off = sim.t
                self.new_cycle_index = 0
                self.current_cycle_index = 2
                temp = 0
                return

    def adjust_green_phase(self, sim, phase, next_phase):
        # Calculate car density for current phase
        if phase == 1:
            cars_density = self.calculate_density([9, 11, 17, 19])  # Roads 1 and 3
        elif phase == 2:
            cars_density = self.calculate_density([8, 10, 16, 18])  # Roads 2 and 4
        elif phase == 3:
            cars_density = self.calculate_density([0, 2])  # Roads 1 and 2
        elif phase == 4:
            cars_density = self.calculate_density([1, 3])  # Roads 3 and 4

        # Adjust cycle length based on car density
        if cars_density < 5:
            setattr(self, f"cycle_length_{phase}", 15)
        elif 5 <= cars_density < 10:
            setattr(self, f"cycle_length_{phase}", 30)
        elif 10 <= cars_density < 15:
            setattr(self, f"cycle_length_{phase}", 45)
        elif 15 <= cars_density <= 20:
            setattr(self, f"cycle_length_{phase}", 60)
        else:
            setattr(self, f"cycle_length_{phase}", 75)

    def calculate_density(self, road_indices):
        # Compute average density of cars on specified roads
        total_density = 0
        for road_index in road_indices:
            total_density += self.traffic_data[road_index][2] + 2 * (
                self.traffic_data[road_index][4] + self.traffic_data[road_index][5]
            )
        return total_density / len(road_indices)
