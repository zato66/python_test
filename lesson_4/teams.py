""" Module Team """
import sys
from typing import Any


def players_repr(players: list[dict], verbose: bool) -> None:
    """Function to represent team"""
    if verbose:
        print("\n>>>>> THE TEAM OF DREAM! <<<<<\n")
        for player in players:
            print(f"{player['name']=}, {player['age']=}, {player['number']=}")
        print("\n>>>>> THE END OF TEAM <<<<<")
    else:
        print("\n")
        for player in players:
            print(f"{player['name']=}, {player['age']=}")


def players_add(players: list[dict], player: dict) -> list[dict]:
    """Function to add player to team"""
    return players.append(player)


def players_del(players: list[dict], name: str) -> list[dict]:
    """Function to delete player from team"""
    for player in players:
        if player["name"] == name:
            print(f"Player {player} was removed")
            players.remove(player)
    return players


def players_find(players: list[dict], field: str, value: Any) -> list[dict]:
    """Function to find player in team"""
    for player in players:
        if player[field] == value:
            return player
    return []


def players_get_by_name(players: list[dict], name: str) -> "dict | None":
    """If multiple players with same name - return the first one."""
    for player in players:
        if player["name"] == name:
            return player
    print("Player not found")
    return None


def main():
    """main function"""
    team = [
        {"name": "John", "age": 20, "number": 1},
        {"name": "Marry", "age": 33, "number": 3},
        {"name": "Cavin", "age": 33, "number": 12},
    ]

    options = ["repr", "add", "del", "find", "get", "exit"]

    while True:
        if not (user_input := input(f"\nEnter your choice {options}: ")):
            break

        if user_input == "add":
            new_player_name = input("\nEnter name of player: ")
            new_player_age = int(input("Enter age of player: "))
            new_player_number = int(input("Enter number of player: "))
            new_player = {
                "name": new_player_name,
                "age": new_player_age,
                "number": new_player_number,
            }
            players_add(team, new_player)

        if user_input == "repr":
            verbose = False
            answer = input("\n'Y' for full info or other button for brief: ")
            if answer == "Y":
                verbose = True
            players_repr(team, verbose)

        if user_input == "del":
            player = input("\nEnter name of player to delete: ")
            team = players_del(team, player)

        if user_input == "get":
            name = input("\nEnter name of player: ")
            player = players_get_by_name(team, name)
            print(player)

        if user_input == "find":
            field = input("\nEnter one of [name, age, number]: ")
            value = input(f"Enter {field} to find: ")
            if field in ("age", "number"):
                value = int(value)
            print(f"Found {players_find(team, field, value)}")

        if user_input == "exit":
            sys.exit(0)


if __name__ == "__main__":
    main()
