import numpy as np

def _degrees_to_radians(degrees):
    # Convert degrees to radians
    return degrees * np.pi / 180

class TrajectoryPropertyFuncs:
    @classmethod
    def MaximumHeight(cls, release_velocity, release_angle, gravitational_acceleration):
        # Calculate the maximum height of the projectile
        release_angle = _degrees_to_radians(release_angle)
        return (release_velocity ** 2) * (np.sin(release_angle)**2) / 2*gravitational_acceleration

    @classmethod
    def TimeOfFlight(cls, release_velocity, release_angle, gravitational_acceleration):
        # Calculate the time of flight of the projectile
        release_angle = _degrees_to_radians(release_angle)
        return (2 * release_velocity * np.sin(release_angle)) / gravitational_acceleration

    @classmethod
    def HorizontalRange(cls, release_velocity, release_angle, gravitational_acceleration):
        # Calculate the horizontal range of the projectile
        release_angle = _degrees_to_radians(release_angle)
        return (release_velocity ** 2) * np.sin(2 * release_angle) / gravitational_acceleration
