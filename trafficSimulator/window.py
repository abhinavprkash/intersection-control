import pygame

from pygame import gfxdraw

import numpy as np

import random
import math
 

class Window:

    def __init__(self, sim, config={}):

        # Simulation to draw

        self.sim = sim

 

        # Set default configurations

        self.set_default_config()

 

        # Update configurations

        for attr, val in config.items():

            setattr(self, attr, val)

       

    def set_default_config(self):

        """Set default configuration"""

        self.width = 1400

        self.height = 900

        self.bg_color = (250, 250, 250)

 

        self.fps = 60

        self.zoom = 5

        self.offset = (0, 0)

 

        self.mouse_last = (0, 0)

        self.mouse_down = False

 

    def loop(self, loop=None):

        """Shows a window visualizing the simulation and runs the loop function."""

       

        # Create a pygame window

        self.screen = pygame.display.set_mode((self.width, self.height))

        pygame.display.flip()

 

        # Fixed fps

        clock = pygame.time.Clock()

 

        # To draw text

        pygame.font.init()

        self.text_font = pygame.font.SysFont('Lucida Console', 16)

 

        # Draw loop

        running = True

        while running:

            # Update simulation

            if loop: loop(self.sim)

 

            # Draw simulation

            self.draw()

 

            # Update window

            pygame.display.update()

            clock.tick(self.fps)

 

            # Handle all events

            for event in pygame.event.get():

                # Quit program if window is closed

                if event.type == pygame.QUIT:

                    running = False

                # Handle mouse events

                elif event.type == pygame.MOUSEBUTTONDOWN:

                    # If mouse button down

                    if event.button == 1:

                        # Left click

                        x, y = pygame.mouse.get_pos()

                        x0, y0 = self.offset

                        self.mouse_last = (x-x0*self.zoom, y-y0*self.zoom)

                        self.mouse_down = True

                    if event.button == 4:

                        # Mouse wheel up

                        self.zoom *=  (self.zoom**2+self.zoom/4+1) / (self.zoom**2+1)

                    if event.button == 5:

                        # Mouse wheel down

                        self.zoom *= (self.zoom**2+1) / (self.zoom**2+self.zoom/4+1)

                elif event.type == pygame.MOUSEMOTION:

                    # Drag content

                    if self.mouse_down:

                        x1, y1 = self.mouse_last

                        x2, y2 = pygame.mouse.get_pos()

                        self.offset = ((x2-x1)/self.zoom, (y2-y1)/self.zoom)

                elif event.type == pygame.MOUSEBUTTONUP:

                    self.mouse_down = False          

 

    def run(self, steps_per_update=1):

        """Runs the simulation by updating in every loop."""

        def loop(sim):

            sim.run(steps_per_update)

        self.loop(loop)

 

    def convert(self, x, y=None):

        """Converts simulation coordinates to screen coordinates"""

        if isinstance(x, list):

            return [self.convert(e[0], e[1]) for e in x]

        if isinstance(x, tuple):

            return self.convert(*x)

        return (

            int(self.width/2 + (x + self.offset[0])*self.zoom),

            int(self.height/2 + (y + self.offset[1])*self.zoom)

        )

 

    def inverse_convert(self, x, y=None):

        """Converts screen coordinates to simulation coordinates"""

        if isinstance(x, list):

            return [self.convert(e[0], e[1]) for e in x]

        if isinstance(x, tuple):

            return self.convert(*x)

        return (

            int(-self.offset[0] + (x - self.width/2)/self.zoom),

            int(-self.offset[1] + (y - self.height/2)/self.zoom)

        )

 

    def background(self, r, g, b):

        """Fills screen with one color."""

        self.screen.fill((r, g, b))

 

    def line(self, start_pos, end_pos, color):

        """Draws a line."""

        gfxdraw.line(

            self.screen,

            *start_pos,

            *end_pos,

            color

        )

 

    def rect(self, pos, size, color):

        """Draws a rectangle."""

        gfxdraw.rectangle(self.screen, (*pos, *size), color)

 

    def box(self, pos, size, color):

        """Draws a rectangle."""

        gfxdraw.box(self.screen, (*pos, *size), color)

 

    def circle(self, pos, radius, color, filled=True):

        gfxdraw.aacircle(self.screen, *pos, radius, color)

        if filled:

            gfxdraw.filled_circle(self.screen, *pos, radius, color)




    def polygon(self, vertices, color, filled=True):

        gfxdraw.aapolygon(self.screen, vertices, color)

        if filled:

            gfxdraw.filled_polygon(self.screen, vertices, color)

 

    def rotated_box(self, pos, size, angle=None, cos=None, sin=None, centered=True, color=(0, 0, 255), filled=True):

        """Draws a rectangle center at *pos* with size *size* rotated anti-clockwise by *angle*."""

        x, y = pos

        l, h = size

 

        if angle:

            cos, sin = np.cos(angle), np.sin(angle)

       

        vertex = lambda e1, e2: (

            x + (e1*l*cos + e2*h*sin)/2,

            y + (e1*l*sin - e2*h*cos)/2

        )

 

        if centered:

            vertices = self.convert(

                [vertex(*e) for e in [(-1,-1), (-1, 1), (1,1), (1,-1)]]

            )

        else:

            vertices = self.convert(

                [vertex(*e) for e in [(0,-1), (0, 1), (2,1), (2,-1)]]

            )

 

        self.polygon(vertices, color, filled=filled)

 

    def rotated_rect(self, pos, size, angle=None, cos=None, sin=None, centered=True, color=(0, 0, 255)):

        self.rotated_box(pos, size, angle=angle, cos=cos, sin=sin, centered=centered, color=color, filled=False)

 

    def arrow(self, pos, size, angle=None, cos=None, sin=None, color=(150, 150, 190)):

        if angle:

            cos, sin = np.cos(angle), np.sin(angle)

       

        self.rotated_box(

            pos,

            size,

            cos=(cos - sin) / np.sqrt(2),

            sin=(cos + sin) / np.sqrt(2),

            color=color,

            centered=False

        )

 

        self.rotated_box(

            pos,

            size,

            cos=(cos + sin) / np.sqrt(2),

            sin=(sin - cos) / np.sqrt(2),

            color=color,

            centered=False

        )

 

    def draw_axes(self, color=(100, 100, 100)):

        x_start, y_start = self.inverse_convert(0, 0)

        x_end, y_end = self.inverse_convert(self.width, self.height)

        self.line(

            self.convert((0, y_start)),

            self.convert((0, y_end)),

            color

        )

        self.line(

            self.convert((x_start, 0)),

            self.convert((x_end, 0)),

            color

        )

 

    def draw_grid(self, unit=50, color=(150,150,150)):

        x_start, y_start = self.inverse_convert(0, 0)

        x_end, y_end = self.inverse_convert(self.width, self.height)

 

        n_x = int(x_start / unit)

        n_y = int(y_start / unit)

        m_x = int(x_end / unit)+1

        m_y = int(y_end / unit)+1

 

        for i in range(n_x, m_x):

            self.line(

                self.convert((unit*i, y_start)),

                self.convert((unit*i, y_end)),

                color

            )

        for i in range(n_y, m_y):

            self.line(

                self.convert((x_start, unit*i)),

                self.convert((x_end, unit*i)),

                color

            )

 

    # def draw_roads(self):

    #     for road in self.sim.roads:

    #         # Draw road background

    #         self.rotated_box(

    #             road.start,

    #             (road.length, 10.7),

    #             cos=road.angle_cos,

    #             sin=road.angle_sin,

    #             color=(180, 180, 220),

    #             centered=False

    #         )

    #         # Draw road lines

    #         # self.rotated_box(

    #         #     road.start,

    #         #     (road.length, 0.25),

    #         #     cos=road.angle_cos,

    #         #     sin=road.angle_sin,

    #         #     color=(0, 0, 0),

    #         #     centered=False

    #         # )

 

    #         # Draw road arrow

    #         if road.length > 5:

    #             for i in np.arange(-0.5*road.length, 0.5*road.length, 10):

    #                 pos = (

    #                     road.start[0] + (road.length/2 + i + 3) * road.angle_cos,

    #                     road.start[1] + (road.length/2 + i + 3) * road.angle_sin

    #                 )

 

    #                 self.arrow(

    #                     pos,

    #                     (-1.25, 0.2),

    #                     cos=road.angle_cos,

    #                     sin=road.angle_sin

    #                 )  

 

    #         # TODO: Draw road arrow
    def draw_roads(self):
        for road in self.sim.roads:
            # Draw road background
            self.rotated_box(
                road.start,
                (road.length, 3.7),
                cos=road.angle_cos,
                sin=road.angle_sin,
                color=(180, 180, 220),
                centered=False
            )

            # Draw road arrow
            if road.length > 5:
                for i in np.arange(-0.5 * road.length, 0.5 * road.length, 10):
                    pos = (
                        road.start[0] + (road.length / 2 + i + 3) * road.angle_cos,
                        road.start[1] + (road.length / 2 + i + 3) * road.angle_sin
                    )

                    self.arrow(
                        pos,
                        (-1.25, 0.2),
                        cos=road.angle_cos,
                        sin=road.angle_sin
                    )

            # Add trees along the road, avoiding intersections
            tree_spacing = 20  # Distance between trees
            tree_offset = 8  # Distance from the road's centerline to the trees
            intersection_margin = 15  # Margin near intersections where no trees are drawn

            for i in np.arange(-0.5 * road.length + intersection_margin,
                            0.5 * road.length - intersection_margin, tree_spacing):
                # Left side tree position
                left_tree_pos = (
                    road.start[0] + (road.length / 2 + i) * road.angle_cos - road.angle_sin * tree_offset,
                    road.start[1] + (road.length / 2 + i) * road.angle_sin + road.angle_cos * tree_offset
                )

                # Right side tree position
                # right_tree_pos = (
                #     road.start[0] + (road.length / 2 + i) * road.angle_cos + road.angle_sin * tree_offset,
                #     road.start[1] + (road.length / 2 + i) * road.angle_sin - road.angle_cos * tree_offset
                # )

                # Draw trees
                # 
                def draw_svg_tree(base_pos, angle_offset=0.1):
                # """
                # Draws an SVG-like tree with the trunk and slanted or upright foliage.
                # :param base_pos: Base position of the tree (where the trunk starts).
                # :param angle_offset: Offset angle for slanting the tree foliage (in radians).
                # """
                    trunk_width = 0.5
                    trunk_height = 2
                    foliage_width = 3
                    foliage_height = 4

                    # Trunk vertices (upright rectangle)
                    trunk_top = (base_pos[0] + trunk_height * road.angle_cos,
                                base_pos[1] + trunk_height * road.angle_sin)
                    trunk_bottom_left = (base_pos[0] - trunk_width * road.angle_sin,
                                        base_pos[1] + trunk_width * road.angle_cos)
                    trunk_bottom_right = (base_pos[0] + trunk_width * road.angle_sin,
                                        base_pos[1] - trunk_width * road.angle_cos)

                    # Foliage vertices (upright or slanted triangle)
                    slant_cos = np.cos(angle_offset)
                    slant_sin = np.sin(angle_offset)

                    foliage_top = (trunk_top[0] + foliage_height * slant_cos * road.angle_cos - foliage_height * slant_sin * road.angle_sin,
                                trunk_top[1] + foliage_height * slant_cos * road.angle_sin + foliage_height * slant_sin * road.angle_cos)
                    foliage_left = (trunk_top[0] - foliage_width * road.angle_sin,
                                    trunk_top[1] + foliage_width * road.angle_cos)
                    foliage_right = (trunk_top[0] + foliage_width * road.angle_sin,
                                    trunk_top[1] - foliage_width * road.angle_cos)

                    # Draw the trunk
                    self.polygon(
                        [
                            self.convert(trunk_bottom_left),
                            self.convert(trunk_bottom_right),
                            self.convert(trunk_top)
                        ],
                        color=(139, 69, 19),  # Brown color
                        filled=True
                    )

                    # Draw the foliage
                    self.polygon(
                        [
                            self.convert(foliage_top),
                            self.convert(foliage_left),
                            self.convert(foliage_right)
                        ],
                        color=(0, 100, 0),  # Green foliage
                        filled=True
                    )


                # Draw SVG-like trees for left and right positions
                draw_svg_tree(left_tree_pos, angle_offset=0.05)  # Slightly slanted
                # draw_svg_tree(right_tree_pos, angle_offset=-0.05)       



 


    def draw_vehicle(self, vehicle, road, type = 'circle'):
        l, h = vehicle.l,  3
        sin, cos = road.angle_sin, road.angle_cos

        x = road.start[0] + cos * vehicle.x 
        y = road.start[1] + sin * vehicle.x 
        radius = vehicle.l / 2 
        if(vehicle.shape == 'circle'):
            self.circle(self.convert((x, y)), int(radius * self.zoom), (0, 0, 255))
        elif(vehicle.shape == 'rectangle'):
            self.rotated_rect((x, y), (l, h), cos=cos, sin=sin, centered=True)
        elif(vehicle.shape == 'triangle'):
            half_base = l / 2
            height = h

            # Calculate vertices relative to the center position (x, y)
            top_vertex = (x + cos * height, y + sin * height)
            bottom_left_vertex = (x - cos * height / 2 - sin * half_base, y - sin * height / 2 + cos * half_base)
            bottom_right_vertex = (x - cos * height / 2 + sin * half_base, y - sin * height / 2 - cos * half_base)

            # Convert vertices to the screen coordinates
            vertices = [
                self.convert(top_vertex),
                self.convert(bottom_left_vertex),
                self.convert(bottom_right_vertex)
            ]

            # Draw the triangle as a polygon
            self.polygon(vertices, (255, 0, 0), filled=True)
        elif(vehicle.shape == 'car'):
            self.car_image = pygame.image.load("/Users/arshgoyal/Desktop/Adaptive-Traffic-Control/car.svg").convert_alpha()  # Load the car image
            self.car_image = pygame.transform.scale(self.car_image, (int(l * 1.4 * self.zoom), int(h * 1.4 * self.zoom)))
            angle = -math.degrees(math.atan2(sin, cos))  # Convert to degrees
            rotated_image = pygame.transform.rotate(self.car_image, angle)
            rect = rotated_image.get_rect(center=self.convert((x, y)))
            self.screen.blit(rotated_image, rect.topleft)
        elif(vehicle.shape == 'truck'):
            self.car_image = pygame.image.load("/Users/arshgoyal/Desktop/Adaptive-Traffic-Control/truck.svg").convert_alpha()  # Load the car image
            self.car_image = pygame.transform.scale(self.car_image, (int(l * 2.4 * self.zoom), int(h * 1.4 * self.zoom)))
            angle = -math.degrees(math.atan2(sin, cos))  # Convert to degrees
            rotated_image = pygame.transform.rotate(self.car_image, angle)
            rect = rotated_image.get_rect(center=self.convert((x, y)))
            self.screen.blit(rotated_image, rect.topleft)
        elif(vehicle.shape == 'bike'):
            self.car_image = pygame.image.load("/Users/arshgoyal/Desktop/Adaptive-Traffic-Control/bike.svg").convert_alpha()  # Load the car image
            self.car_image = pygame.transform.scale(self.car_image, (int(l * 1.4 * self.zoom), int(h * 1.4 * self.zoom)))
            angle = -math.degrees(math.atan2(sin, cos))  # Convert to degrees
            rotated_image = pygame.transform.rotate(self.car_image, angle)
            rect = rotated_image.get_rect(center=self.convert((x, y)))
            self.screen.blit(rotated_image, rect.topleft)

    def draw_vehicles(self):

        for road in self.sim.roads:

            # Draw vehicles

            for vehicle in road.vehicles:

                self.draw_vehicle(vehicle, road)

 

    def draw_signals(self):

        for signal in self.sim.traffic_signals:

            for i in range(len(signal.roads)):

                color = (0, 255, 0) if signal.current_cycle[i] else (255, 0, 0)

                for road in signal.roads[i]:

                    a = 0

                    position = (

                        (1-a)*road.end[0] + a*road.start[0],        

                        (1-a)*road.end[1] + a*road.start[1]

                    )

                    self.rotated_box(

                        position,

                        (1, 3),

                        cos=road.angle_cos, sin=road.angle_sin,

                        color=color)

 

    def draw_status(self):

        text_fps = self.text_font.render(f't={self.sim.t:.2f}s', False, (0, 0, 0))

        text_frc = self.text_font.render(f'n={self.sim.frame_count}', False, (0, 0, 0))

        text_cars = self.text_font.render(f'Vehicles passed: {self.sim.traffic_signals[0].vehicles_passed}', False, (0, 0, 0))

       

        self.screen.blit(text_fps, (0, 0))

        self.screen.blit(text_frc, (100, 0))

        self.screen.blit(text_cars, (0, 30))

    def draw_grassland(self):
        """Draws a green grassland background with fixed dots for texture."""
        # Fill the entire screen with a green base color
        self.screen.fill((34, 139, 34))  # Green color for grassland

        # Add fixed dots to simulate grass texture
        dot_spacing = 20  # Spacing between dots
        dot_size = 1  # Size of the dots
        dot_colors = [(0, 100, 0), (0, 128, 0), (0, 150, 0)]  # Varying shades of green

        for x in range(0, self.width, dot_spacing):
            for y in range(0, self.height, dot_spacing):
                color = dot_colors[(x + y) % len(dot_colors)]  # Cycle through fixed colors
                pygame.draw.circle(self.screen, color, (x, y), dot_size)


    def draw(self):

        # Fill background

        # self.background(*self.bg_color)
        self.draw_grassland()

 

        # Major and minor grid and axes

        # self.draw_grid(10, (220,220,220))

        # self.draw_grid(100, (200,200,200))

        # self.draw_axes()

 

        self.draw_roads()

        self.draw_vehicles()

        self.draw_signals()

 

        # Draw status info

        self.draw_status()

       