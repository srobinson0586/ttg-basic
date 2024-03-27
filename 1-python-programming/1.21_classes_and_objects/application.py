#!/bin/python
# Python Classes and Objects - Application

# 1. TODO: Create a class called `Game` according to the `Game` docstring:
class Game():
    """
    The `Game` class should be a template for a sports game where two teams are in a competition for points. 

    Attributes:
        - team1_name: str; The name of the first team in the game.
        - team1_points: int; The number of points that the first team has.
        - team2_name: str; The name of the second team in the game.
        - team2_points: int; The number of points that the second team has.

    Methods:
        - __init__

            Constructor for instances of `Game`.

            If not provided, `team1_name` should be set to "Red", `team2_name` should be set to "Blue", and points for both teams should be set to 0.

            Parameters:
                - self
                - team1_name: str; The value to initialize the first team's name as.
                - team1_points: int; The value to initialize the first team's points as.
                - team2_name: str; The value to initialize the second team's name as.
                - team2_points: int; The value to initialize the second team's points as.

            Returns:
                This function should not return a value.

            Example:
            >>> game1 = Game(team1_name="Joint Cyber", team1_points=0, team2_name="Maritime Cyber", team2_points = 0)

                
        - winner

            Compares the scores of each team and determines who the winner of the game is. If each team has an equal amount of points, the message should indicate a draw.

            Parameters:
                - self
            
            Returns:
                - str: A message formatted as follows
                    <team_name> won!
                    OR
                    Draw

            Example:
            >>> winner_message = game1.winner()
            >>> print(winner_message)
            Joint Cyber won!
            >>> draw_message = game2.winner()
            >>> print(draw_message)
            Draw
    """
    pass


# 2. TODO: Create a class called `BasketballGame` which inherits from `Game` and extends attributes and methods according to the `BasketballGame` docstring:
class BasketballGame(Game):
    """
    The `BasketballGame` class should inherit from `Game` and be a rough template to represent a Basketball game.

    Attributes:
        - team1_name: str; The name of the first team in the game.
        - team1_points: int; The number of points that the first team has.
        - team1_timeouts: int; The number of timeouts the first team has.
        - team2_name: str; The name of the second team in the game.
        - team2_points: int; The number of points that the second team has.
        - team2_timeouts: int; The number of timeouts the second team has.

    Methods:
        - __init__

            Constructor for instances of `BasketballGame`.

            This constructor should make use of the parent's constructor using the `super` function to initialize the four attributes inherited from the parent. If not provided, the four inherited attributes should be initialized to the same default values as the parent, and `team1_timeouts` and `team2_timeouts` should be initialized to 3.

            Parameters:
                - self
                - team1_name: str; The value to initialize the first team's name as.
                - team1_points: int; The value to initialize the first team's points as.
                - team1_timeouts: int; The value to initialize the first team's number of timeouts as.
                - team2_name: str; The value to initialize the second team's name as.
                - team2_points: int; The value to initialize the second team's points as.
                - team2_timeouts: int; The value to initialize the second team's number of timeouts as.

            Returns:
                This function should not return a value.

            Example:
            >>> game1 = BasketballGame(team1_name="Joint Cyber", team1_points=0, team1_timeouts=3, team2_name="Maritime Cyber", team2_points=0, team2_timeouts=3)

                
        - add_points

            Adds points to the `team1_points` or `team2_points` according to the `scoring_team` parameter. The number of points to be added will depend on the `score_type` parameter.

            Parameters:
                - self
                - score_type: str; A string indicating the type of score.
                    "3ptr"         = 3 points
                    "2ptr"         = 2 points
                    "free throw"  = 1 point
                    other         = 0 points
                - scoring_team: int; The integer 1 or 2 to represent the scoring team as team1 or team2.
            
            Returns:
                This function should not return a value.

            Example:
            >>> game1.add_points("3ptr", scoring_team=1)
            >>> game1.add_points("free throw", scoring_team=2)

            
        - call_timeout

            Prints a message that a timeout has been called by a team. Decrements the number of timeouts for that team by 1. If the team does not have any timeouts remaining, the number of timeouts should not be decremented and a message should print out indicating that the team does not have any timeouts.

            Parameters:
                - self
                - team: int; The integer 1 or 2 to represent the team calling the timeout.
            
            Returns:
                This function should not return a value.

            Example:
            >>> game1.call_timeout(team=1)
            <team1_name> called a timeout.
            >>> game1.call_timeout(team=2)
            <team2_name> cannot call timeout!
    """
    pass
