import math

### max speed = max_engine_speed / mass / drag.
### max acceleration = max_engine_speed / mass

class Ship:
    """ A class representing US Navy warships.

    There are 4 currently supported classes:
        1. DDG
        2. LCS
        3. CVN
        4. LPD

    Each Ship instance has the following attributes:
        1. name (str): The name of the ship.
        2. cls  (str): The class of the ship.
        3. location (tuple of 2 numbers): The x- and y-coordinates of the ship
           in nautical miles, relative to where they started.
        4. heading (number): The heading of the ship in degrees from North.
        5. rudder_angle (number): The current angle of the rudder in degrees
           from center.
        6. speed (number): The speed of the ship in knots.
        7. engine_speed (number): The current speed of the engine in thousands
           of RPM. """

    maneuverability_dict = {"DDG": 0.0003,
                            "LCS": 0.0006,
                            "CVN": 0.0001,
                            "LPD": 0.0001}

    max_engine_speed_dict = {"DDG": 70,
                             "LCS": 50,
                             "CVN": 150,
                             "LPD": 60}

    mass_dict = {"DDG": 200,
                 "LCS": 120,
                 "CVN": 350,
                 "LPD": 300}

    drag_dict = {"DDG": 1/100,
                 "LCS": 1/70,
                 "CVN": 1/120,
                 "LPD": 1/150}

    def __init__(self, name, cls):
        """ Create a new ship. """
        ### TODO: Initialize all attributes: name, cls, location,
        ### heading, rudder_angle, speed, and engine_speed.
        ### - Verify that `cls` is a valid key in the dictionaries above.
        ###   If not, raise a ValueError.
        ### - Initialize all attributes that aren't passed to __init__
        ###   to 0.
    def __str__(self):
        """ This is the magic method that will be called to generate the
        output when print() is called on a Ship. """
        ### TODO: Return a string that displays all information about the
        ### ship in a nice format.
        rtn = ""        
        return rtn


    def get_maneuverability(self):
        """ Return the ship's maneuverability (determines how fast it can
        turn) based on it's class. """
        ### TODO
    def get_max_engine_speed(self):
        """ Return the ship's max engine speed based on its class. """
        ### TODO
    def get_drag(self):
        """ Return the ship's drag (determines how strongly it wants to slow
        down) based on its class. """
        ### TODO
    def get_mass(self):
        """ Return the ship's mass (determines how resistant the ship is to
        change in speed) based on its class. """
        ### TODO
    def get_turning_rate(self):
        """ Determine the rate of turning (in degrees per second) of
        the ship. This will be proportional to the rudder angle, the speed,
        and the natural maneuverability of the ship. """
        rudder_wash_speed = self.speed + self.engine_speed
        turning_rate = rudder_wash_speed * self.rudder_angle * self.get_maneuverability()
        return turning_rate

    def set_rudder_angle(self, new_angle):
        """ Set the new rudder angle.
        The rudder cannot move more than 40 degrees in either direction.
        If `new_angle` is outside this range, return False and do not update.
        Otherwise, update and return True. """
        ### TODO
    def set_engine_speed(self, new_engine_speed):
        """ Set the new engine speed.
        The engine speed is limited to between 0 and the maximum
        engine speed for the ship's class.
        If `new_engine_speed` is outside this range, return False and
        do not update. Otherwise update and return True. """
        ### TODO
    def set_max_engine_speed(self):
        """ Set the engine speed to its maximum possible value. """
        ### TODO
    def update(self, t_secs):
        """ Update the location, heading, and speed to simulate `t_secs`
        seconds of operation with the current conditions. """
        t_hours = t_secs / 3600

        ### Update location based on current speed.
        delta_x = math.cos(self.heading / 180 * math.pi) * self.speed * t_hours
        delta_y = math.sin(self.heading / 180 * math.pi) * self.speed * t_hours
        ### TODO: Update `self.location` by adding `delta_x` to the x-coordinate
        ### and `delta_y` to the y-coordinate.
        ### Update heading based on current turning rate.
        ### TODO: Update `self.heading` by adding the turning rate times
        ### the number of seconds we're turning for.        ### TODO: Update `self.heading` to be between 0 and 360 using the
        ### modulus operator.
        ### Decrease speed based on drag.
        self.speed -= self.speed * self.get_drag()
        ### Increase speed based on engine speed.
        self.speed += self.engine_speed / self.get_mass()

class Fleet:
    """ A class that represents a US Navy fleet.

    The main feature is a list of Ship instances. """

    def __init__(self, name):
        """ Initialize a new empty fleet. """
        ### TODO: Initialize the attributes: name and ships.
        ### Initially there are no ships in the fleet.
    def __str__(self):
        """ This is the magic method that will be called to generate the
        output when print() is called on a Fleet. """
        ### TODO: Return a string representation of all ships in the fleet.
        ### Hint: You can use the __str__ method of the ships!
    def add_ship(self, ship):
        """ Add the ship to the fleet. """
        ### TODO
    def update(self, t_secs):
        """ Update all ships in the fleet by the indicated time step. """
        ### TODO
def main():
    fleet = Fleet("US 10th Fleet")

    ddg = Ship("Paul Jones", "DDG")
    ddg.set_rudder_angle(10)
    ddg.set_max_engine_speed()
    print(ddg)
    fleet.add_ship(ddg)

    lcs = Ship("Savannah", "LCS")
    lcs.set_rudder_angle(30)
    lcs.set_max_engine_speed()
    print(lcs)
    fleet.add_ship(lcs)

    cvn = Ship("Teddy Roosevelt", "CVN")
    cvn.set_rudder_angle(0)
    cvn.set_max_engine_speed()
    print(cvn)
    fleet.add_ship(cvn)

    lpd = Ship("Coronado", "LPD")
    lpd.set_rudder_angle(-30)
    lpd.set_max_engine_speed()
    print(lpd)
    fleet.add_ship(lpd)

    print()
    print(fleet)

    t = 0
    for i in range(10):
        t += 1
        fleet.update(1)

    print("t =", t)
    print(fleet)

    for i in range(290):
        t += 1
        fleet.update(1)

    print("t =", t)
    print(fleet)


if __name__ == "__main__":
    main()
