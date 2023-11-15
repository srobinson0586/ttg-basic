#!/bin/python
# Python Competency 5 Ship - Pytest Suite
import pytest
import ship
        
def test_ship():
    # Testing constructor for ship
    my_ddg = ship.Ship("Black Pearl", "DDG")
    assert my_ddg.name == "Black Pearl", "`name` not correctly set for new instances of `Ship`"
    assert my_ddg.cls == "DDG", "`cls` not correctly set for new instances of `Ship`"
    assert my_ddg.location == (0, 0), "`location` not correctly set for new instances of `Ship`"
    assert my_ddg.heading == 0, "`heading` not correctly set for new instances of `Ship`"
    assert my_ddg.rudder_angle == 0, "`rudder_angle not correctly set for new instances of `Ship`"
    assert my_ddg.engine_speed == 0, "`engine_speed` not correctly set for new instances of `Ship`"

    # Testing invalid `cls` raises `ValueError`
    with pytest.raises(ValueError) as ve:
        invalid_ship = ship.Ship("Invalid Ship", "Invalid Class")
    assert ve.type is ValueError

    # Testing __str__ displays all attributes of a ship
    ship_info = str(my_ddg)
    assert my_ddg.name in ship_info, "`name` not returned as part of __str__"
    assert my_ddg.cls in ship_info, "`cls` not returned as part of __str__"
    assert str(my_ddg.location) in ship_info, "`location` not returned as part of __str__"
    assert str(my_ddg.heading) in ship_info, "`heading` not returned as part of __str__"
    assert str(my_ddg.rudder_angle) in ship_info, "`rudder_angle` not returned as part of __str__"
    assert str(my_ddg.engine_speed) in ship_info, "`engine_speed` not returned as part of __str__"

    # Testing getter methods
    assert my_ddg.maneuverability_dict[my_ddg.cls] == my_ddg.get_maneuverability(), "`get_maneuverability` returns incorrect value"
    assert my_ddg.max_engine_speed_dict[my_ddg.cls] == my_ddg.get_max_engine_speed(), "`get_max_engine_speed` returns incorrect value"
    assert my_ddg.drag_dict[my_ddg.cls] == my_ddg.get_drag(), "`get_drag` returns incorrect value"
    assert my_ddg.mass_dict[my_ddg.cls] == my_ddg.get_mass(), "`get_mass` returns incorrect value"
    
    # Testing setter methods for DDG
    assert my_ddg.set_engine_speed(-1) == False, "`set_engine_speed` allows negative values"
    assert my_ddg.set_engine_speed(10000) == False, "`set_engine_speed` allows values exceeding the max engine speed for the ship class"
    assert my_ddg.set_engine_speed(20) == True, "`set_engine_speed` does not correctly set a valid engine speed"

    assert my_ddg.set_rudder_angle(-41) == False, "'set_rudder_angle` allows for a rudder angle exceeding -40 degrees"
    assert my_ddg.set_rudder_angle(41) == False, "'set_rudder_angle` allows for a rudder angle exceeding 40 degrees"
    assert my_ddg.set_rudder_angle(25) == True, "'set_rudder_angle` does not correctly set a valid rudder angle"

    my_ddg.set_max_engine_speed()
    assert 70 == my_ddg.max_engine_speed_dict[my_ddg.cls], "`set_max_engine_speed` does not correctly set the engine speed"


    # Testing setter methods for LCS
    my_lcs = ship.Ship("My LCS", "LCS")
    assert my_lcs.set_engine_speed(-1) == False, "`set_engine_speed` allows negative values"
    assert my_lcs.set_engine_speed(10000) == False, "`set_engine_speed` allows values exceeding the max engine speed for the ship class"
    assert my_lcs.set_engine_speed(20) == True, "`set_engine_speed` does not correctly set a valid engine speed"

    assert my_lcs.set_rudder_angle(-41) == False, "'set_rudder_angle` allows for a rudder angle exceeding -40 degrees"
    assert my_lcs.set_rudder_angle(41) == False, "'set_rudder_angle` allows for a rudder angle exceeding 40 degrees"
    assert my_lcs.set_rudder_angle(25) == True, "'set_rudder_angle` does not correctly set a valid rudder angle"

    my_lcs.set_max_engine_speed()
    assert 50 == my_lcs.max_engine_speed_dict[my_lcs.cls], "`set_max_engine_speed` does not correctly set the engine speed"

    # Testing setter methods for CVN
    my_cvn = ship.Ship("My CVN", "CVN")
    assert my_cvn.set_engine_speed(-1) == False, "`set_engine_speed` allows negative values"
    assert my_cvn.set_engine_speed(10000) == False, "`set_engine_speed` allows values exceeding the max engine speed for the ship class"
    assert my_cvn.set_engine_speed(20) == True, "`set_engine_speed` does not correctly set a valid engine speed"

    assert my_cvn.set_rudder_angle(-41) == False, "'set_rudder_angle` allows for a rudder angle exceeding -40 degrees"
    assert my_cvn.set_rudder_angle(41) == False, "'set_rudder_angle` allows for a rudder angle exceeding 40 degrees"
    assert my_cvn.set_rudder_angle(25) == True, "'set_rudder_angle` does not correctly set a valid rudder angle"

    my_cvn.set_max_engine_speed()
    assert 150 == my_cvn.max_engine_speed_dict[my_cvn.cls], "`set_max_engine_speed` does not correctly set the engine speed"

    # Testing setter methods for LPD
    my_lpd = ship.Ship("My LPD", "LPD")
    assert my_lpd.set_engine_speed(-1) == False, "`set_engine_speed` allows negative values"
    assert my_lpd.set_engine_speed(10000) == False, "`set_engine_speed` allows values exceeding the max engine speed for the ship class"
    assert my_lpd.set_engine_speed(20) == True, "`set_engine_speed` does not correctly set a valid engine speed"

    assert my_lpd.set_rudder_angle(-41) == False, "'set_rudder_angle` allows for a rudder angle exceeding -40 degrees"
    assert my_lpd.set_rudder_angle(41) == False, "'set_rudder_angle` allows for a rudder angle exceeding 40 degrees"
    assert my_lpd.set_rudder_angle(25) == True, "'set_rudder_angle` does not correctly set a valid rudder angle"

    my_lpd.set_max_engine_speed()
    assert 60 == my_lpd.max_engine_speed_dict[my_lpd.cls], "`set_max_engine_speed` does not correctly set the engine speed"

    # Testing `update` method functionality
    new_cvn = ship.Ship("New CVN", "CVN")
    new_cvn.set_rudder_angle(15)
    new_cvn.set_max_engine_speed()
    new_cvn.update(600)
    assert new_cvn.heading == 135.0, "`update` function not setting `heading` correctly"
    assert new_cvn.location == (0, 0), "`update` function not correctly updating `location`"
    new_cvn.update(600)
    assert new_cvn.heading >= 270 and new_cvn.heading <= 270.4, "`update` function not setting `heading` correctly"
    assert new_cvn.location[0] < -0.049 and new_cvn.location[0] > -0.051, "`update` function not correctly updating `location`"
    assert new_cvn.location[1] > 0.049 and new_cvn.location[1] < 0.051, "`update` function not correctly updating `location`"

    # Testing Fleet constructor
    my_fleet = ship.Fleet("My Fleet")
    assert my_fleet.name == "My Fleet", "`name` not correctly set for new Fleet instances"
    assert my_fleet.ships == [], "`ships` not initialized as an empty list for new Fleet instances"

    # Testing `add_ship` for Fleet
    fleet_cvn1 = ship.Ship("cvn1", "CVN")
    fleet_cvn2 = ship.Ship("cvn2", "CVN")
    my_fleet.add_ship(fleet_cvn1)
    my_fleet.add_ship(fleet_cvn2)
    assert my_fleet.ships[0] == fleet_cvn1, "`add_ship` does not properly add new ships for Fleet instances"
    assert my_fleet.ships[1] == fleet_cvn2, "`add_ship` does not properly add new ships for Fleet instances"

    # Testing Fleet __str__ prints information for all ships
    fleet_output = str(my_fleet)
    assert "cvn1" in fleet_output and "cvn2" in fleet_output, "`__str__` does not print out data for all ships"

    # Testing Fleet `update`
    fleet_cvn1.set_rudder_angle(15)
    fleet_cvn1.set_max_engine_speed()
    fleet_cvn2.set_rudder_angle(15)
    fleet_cvn2.set_max_engine_speed()
    my_fleet.update(600)
    assert fleet_cvn1.heading == 135.0, "`update` function for Fleet not updating ships"
    assert fleet_cvn1.location == (0, 0), "`update` function for Fleet not updating ships"
    assert fleet_cvn2.heading == 135.0, "`update` function for Fleet not updating ships"
    assert fleet_cvn2.location == (0, 0), "`update` function for Fleet not updating ships"
    my_fleet.update(600)
    assert fleet_cvn1.heading >= 270 and fleet_cvn1.heading <= 270.4, "`update` function for Fleet not updating ships"
    assert fleet_cvn1.location[0] < -0.049 and fleet_cvn1.location[0] > -0.051, "`update` function for Fleet not updating ships"
    assert fleet_cvn1.location[1] > 0.049 and fleet_cvn1.location[1] < 0.051, "`update` function for Fleet not updating ships"
    assert fleet_cvn2.heading >= 270 and fleet_cvn1.heading <= 270.4, "`update` function for Fleet not updating ships"
    assert fleet_cvn2.location[0] < -0.049 and fleet_cvn1.location[0] > -0.051, "`update` function for Fleet not updating ships"
    assert fleet_cvn2.location[1] > 0.049 and fleet_cvn1.location[1] < 0.051, "`update` function for Fleet not updating ships"



