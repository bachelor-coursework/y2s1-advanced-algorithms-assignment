from Q2.classes.Graph import Graph
from Q2.classes.Person import Person
from Q2.people_data import people

import cli_menu


def _concat_user_names(users: list[Person]):
    return_string = ""
    for user in users:
        return_string += f"[{user.id}] {user.name}\n"
    return return_string


def list_all_users_menu(graph: Graph):
    users = graph.get_all_vertices()
    input(_concat_user_names(users))


def view_profile_details_menu(graph: Graph):
    input_user_id = input("Enter user id: ")
    if input_user_id not in graph.vertex_lookup.keys():
        input("User not found.")
        return
    user = graph.vertex_lookup[input_user_id]

    cli_menu.clear_screen()
    while True:
        followers = graph.list_incoming_adjacent_vertex(user)
        following = graph.list_outgoing_adjacent_vertex(user)
        print(user)
        print("-" * 20)
        print(f"Followers:\n{_concat_user_names(followers) or "no one"}")
        print("-" * 20)
        print(f"Following:\n{_concat_user_names(following) or "no one"}")
        print("-" * 50)
        exit_menu = profile_details_edit_menu(graph, user)
        cli_menu.clear_screen()

        if exit_menu:
            break


def profile_details_edit_menu(graph: Graph, user: Person) -> bool:
    choice = cli_menu.select(title="Actions", choices=["Follow someone", "Unfollow someone", "Exit"])

    # exit immediately if choice is 3
    if choice == "3":
        return True

    # search up user to follow / unfollow
    input_user_id = input("Enter user id: ")
    if input_user_id not in graph.vertex_lookup.keys():
        input("User not found.")
        return
    input_user = graph.vertex_lookup[input_user_id]

    # follow someone
    following = graph.list_outgoing_adjacent_vertex(user)
    if choice == "1":
        if input_user in following:
            input(f"You are already following {input_user.name}.")
        else:
            # confirmation
            print("Follow this user?")
            print(input_user)
            confirm = cli_menu.input_bool("(y/n): ")

            if confirm:
                graph.add_edge(user, input_user)
                input(f"You followed {input_user.name}.")
            else:
                input("Canceled.")

    # unfollow someone
    elif choice == "2":
        if input_user not in following:
            input(f"You are not currently following {input_user.name}.")
        else:
            # confirmation
            print("Unfollow this user?")
            print(input_user)
            confirm = cli_menu.input_bool("(y/n): ")

            if confirm:
                graph.remove_edge(user, input_user)
                input(f"You unfollowed {input_user.name}.")
            else:
                input("Canceled.")

    cli_menu.clear_screen()


def main():
    graph = Graph()
    graph.vertex_lookup = people

    graph.add_edge(people["0001"], people["0009"])
    graph.add_edge(people["0003"], people["0010"])
    graph.add_edge(people["0003"], people["0005"])
    graph.add_edge(people["0003"], people["0010"])
    graph.add_edge(people["0004"], people["0002"])
    graph.add_edge(people["0004"], people["0007"])
    graph.add_edge(people["0005"], people["0001"])
    graph.add_edge(people["0006"], people["0003"])
    graph.add_edge(people["0007"], people["0010"])
    graph.add_edge(people["0008"], people["0009"])
    graph.add_edge(people["0009"], people["0003"])

    while True:
        choice = cli_menu.select(title="Social Media Graph View", choices=["List all users", "View profile details"])
        match choice:
            case "1":
                list_all_users_menu(graph)
            case "2":
                view_profile_details_menu(graph)
        cli_menu.clear_screen()


if __name__ == "__main__":
    main()
