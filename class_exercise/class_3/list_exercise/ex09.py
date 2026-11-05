
players_names_and_scores_info ={}

tuple_list_player_info = []

menu_options = ["Y", "N"]

while True:
    while True:
        try:
            player_name = input(
                "Please, enter your name: "
                ).strip()

            if not player_name:
                raise ValueError\
            ("Please, enter a valid name.\n")
            break
        
        except ValueError as e:
            print(f">>> ERROR >>> {e}")   

    while True:
        try:
            raw_score = input("Please enter your score: ")

            if "." in raw_score and "," in raw_score:
                raw_score = raw_score.replace(".", "")

            clean_score = raw_score.replace(",", ".")

            score = float(clean_score)

            players_names_and_scores_info[player_name] = score
            break
                
        except ValueError as e:
                print(f">>> ERROR >>> {e}")

    while True:
            end_of_log = (input("Do you want to register "
                    "more player(s)\n [Y]-yes \n [N]-no\n"
                    "option: ")).upper()

            if not end_of_log in menu_options:
                print("Please, choose a valid option [Y] [N]")
                continue
            break
    
    if end_of_log == "N":
         break
    
          
players_list_info = list(players_names_and_scores_info.items())

players_list_info.sort(key=lambda player: player[1], reverse=True)

top_3_players = players_list_info[:3]

for position, (name, score) in enumerate(top_3_players, start=1):
    print(f"{position}º lugar: {name} - {score:.0f} pontos")