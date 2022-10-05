first_line = input().split(" ")
second_line = input().split(" ")
third_line = input().split(" ")
first_player = False
second_player = False
if first_line[0] == first_line[1] == first_line[2] == "1":
    first_player = True
elif second_line[0] == second_line[1] == second_line[2] == "1":
    first_player = True
elif third_line[0] == third_line[1] == third_line[2] == "1":
    first_player = True
elif first_line[0] == second_line[0] == third_line[0] == "1":
    first_player = True
elif first_line[1] == second_line[1] == third_line[1] == "1":
    first_player = True
elif first_line[2] == second_line[2] == third_line[2] == "1":
    first_player = True

elif first_line[0] == second_line[1] == third_line[2] == "1":
    first_player = True
elif first_line[2] == second_line[1] == third_line[0] == "1":
    first_player = True

elif first_line[0] == first_line[1] == first_line[2] == "2":
    second_player = True
elif second_line[0] == second_line[1] == second_line[2] == "2":
    second_player = True
elif third_line[0] == third_line[1] == third_line[2] == "2":
    second_player = True
elif first_line[0] == second_line[0] == third_line[0] == "2":
    second_player = True
elif first_line[1] == second_line[1] == third_line[1] == "2":
    second_player = True
elif first_line[2] == second_line[2] == third_line[2] == "2":
    second_player = True

elif first_line[0] == second_line[1] == third_line[2] == "2":
    second_player = True
elif first_line[2] == second_line[1] == third_line[0] == "2":
    second_player = True
if first_player:
    print("First player won")
elif second_player:
    print("Second player won")
else:
    print("Draw!")
