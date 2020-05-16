import numpy as np
from typing import List, Optional
from Ball import Ball

class SystemState:
    time: float
    current_objects_in_collision = None
    balls_location: np.ndarray
    balls_velocity: np.ndarray
    balls_angle: np.ndarray
    balls_angular_velocity: np.ndarray

    def get_collision_description(self) -> str:
        ret_str = "not implemented"
        if self.current_objects_in_collision is None:
            ret_str = "description for collition of more than two objects is not implemented"
        if len(self.current_objects_in_collision) == 2:
            b1: Optional[Ball] = None
            b2: Optional[Ball] = None
            wall_key: object = None
            collider1 = "Non"
            collider2 = "Non"
            approximate_location = "Non"
            if type(self.current_objects_in_collision[0]) == Ball:
                b1 = self.current_objects_in_collision[0]
                if type(self.current_objects_in_collision[1]) == Ball:
                    b2 = self.current_objects_in_collision[1]
                else:
                    wall_key = self.current_objects_in_collision[1]
            elif type(self.current_objects_in_collision[1]) == Ball:
                b1 = self.current_objects_in_collision[1]
                b2 = None
                wall_key = self.current_objects_in_collision[0]
            if b1 is not None:
                collider1 = "ball: " + str(b1.id)
            if b2 is not None:
                # two ball interaction
                collider2 = "ball: " + str(b2.id)
                approximate_location = (b1.location + b2.location)/2
            elif wall_key is not None:
                # ball and wall interaction
                collider2 = "wall: " + str(wall_key)
                approximate_location = b1.location
            ret_str = "interaction between " + collider1 + " and " + collider2 + ". at approximate coordinates: " + str(approximate_location)
        else:
            raise NotImplementedError("unrecognized collision type, please implement function - get_collision_description in class SystemState")
        return ret_str

    @staticmethod
    def generate_from_balls_array(time:float, current_objects_in_collision, balls:List[Ball]):
        self = SystemState()
        self.time = time
        self.current_objects_in_collision = current_objects_in_collision
        self.balls_location = np.array([ball.location for ball in balls])
        self.balls_velocity = np.array([ball.velocity for ball in balls])
        self.balls_angle = np.array([ball.angle for ball in balls])
        self.balls_angular_velocity = np.array([ball.angular_vel for ball in balls])
        return self