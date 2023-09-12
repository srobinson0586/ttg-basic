#!/bin/python
# Python Classes and Objects - Pytest Suite
import application
        
def test_game():
    # Testing default values and draw result of `winner`
    my_game = application.Game()
    assert my_game.team1_name == "Red", "Default `team1_name is not \"Red\""
    assert my_game.team2_name == "Blue", "Default `team2_name is not \"Red\""
    assert my_game.team1_points == 0, "Default value for `team1_points` is not 0"
    assert my_game.team2_points == 0, "Default value for `team2_points` is not 0"
    assert my_game.winner() == "Draw", "The result was not a draw when each team had the same number of points"

    # Testing constructor with arguments and checking winner logic for first team as the winner
    game2 = application.Game(team1_name="Devs", team1_points=102, team2_name="Admin", team2_points=100)
    assert game2.team1_name == "Devs", "`team1_name` not properly set when passed into constructor"
    assert game2.team2_name == "Admin", "`team2_name` not properly set when passed into constructor"
    assert game2.team1_points == 102, "`team1_points` not properly set when passed into constructor"
    assert game2.team2_points == 100, "`team2_points` not properly set when passed into constructor"
    assert game2.winner() == "Devs win!", "`winner` logic is incorrect when first team wins"

    # Testing inheritance and child class constructor default arguments
    game3 = application.BasketballGame()
    assert game3.team1_name == "Red", "In child class, default `team1_name is not \"Red\""
    assert game3.team2_name == "Blue", "In child class, default `team2_name is not \"Red\""
    assert game3.team1_points == 0, "In child class, default value for `team1_points` is not 0"
    assert game3.team2_points == 0, "In child class, default value for `team2_points` is not 0"
    assert game3.team1_timeouts == 3, "In child class, default value for `team1_timeouts` is not 3"
    assert game3.team2_timeouts == 3, "In child class, default value for `team1_timeouts` is not 3"

    # Testing inheritance and child class constructor with arguments
    game4 = application.BasketballGame(team1_name="Suns", team1_points=50, team2_timeouts=6, team2_name="Warriors", team2_points=61, team1_timeouts=6)
    assert game4.team1_name == "Suns", "In child class, `team1_name` not properly set when passed into constructor"
    assert game4.team2_name == "Warriors", "In child class, `team2_name` not properly set when passed into constructor"
    assert game4.team1_points == 50, "In child class, `team1_points` not properly set when passed into constructor"
    assert game4.team2_points == 61, "In child class, `team2_points` not properly set when passed into constructor"
    assert game4.team1_timeouts == 6, "In child class, `team1_timeouts` not properly set when passed into constructor"
    assert game4.team2_timeouts == 6, "In child class, `team2_timeouts` not properly set when passed into constructor"

    # Testing child class functionality
    game4.team1_points = 50
    game4.add_points(1, "free throw")
    assert game4.team1_points == 51, "Points not correctly added to `team1_points` for \"free throw\" score type"
    game4.team1_points = 50
    game4.add_points(1, "2ptr")
    assert game4.team1_points == 52, "Points not correctly added to `team1_points` for \"2ptr\" score type"
    game4.team1_points = 50
    game4.add_points(1, "3ptr")
    assert game4.team1_points == 53, "Points not correctly added to `team1_points` for \"3ptr\" score type"
    
    game4.team2_points = 61
    game4.add_points(2, "free throw")
    assert game4.team2_points == 62, "Points not correctly added to `team2_points` for \"free throw\" score type"
    game4.team2_points = 61
    game4.add_points(2, "2ptr")
    assert game4.team2_points == 63, "Points not correctly added to `team2_points` for \"2ptr\" score type"
    game4.team2_points = 61
    game4.add_points(2, "3ptr")
    assert game4.team2_points == 64, "Points not correctly added to `team2_points` for \"3ptr\" score type"
    
    game4.team1_timeouts = 6
    game4.call_timeout(1)
    assert game4.team1_timeouts == 5, "Timeouts not decremented for `team1_timeouts`"
    game4.team1_timeouts = 0
    game4.call_timeout(1)
    assert game4.team1_timeouts == 0, "Timeout called even though `team1_timeouts` was 0"
    
    game4.team2_timeouts = 6
    game4.call_timeout(2)
    assert game4.team2_timeouts == 5, "Timeouts not decremented for `team2_timeouts`"
    game4.team2_timeouts = 0
    game4.call_timeout(2)
    assert game4.team2_timeouts == 0, "Timeout called even though `team2_timeouts` was 0"

    assert game4.winner() == "Warriors win!", "`winner` logic is incorrect when second team wins"
