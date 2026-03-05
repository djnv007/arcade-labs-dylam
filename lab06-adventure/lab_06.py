import json
class Room:
    def __init__(self,room,description, north, south, east,west):
        self.room=room
        self.description=description 
        self.north=north
        self.east =east
        self.south=south
        self.west=west
def main():
    read_list=json.load(open("room.json", encoding="utf-8"))
    room_list=[]
    for room in read_list:
        room=Room(room["room"], room["description"], room["north"], room["south"], room["east"], room["west"])
        room_list.append(room)
    current_room=0
    done=False
    print("to exit , type exit or quit")
    while (done==False):
        print("")
        print(f"{room_list[current_room].room}:")
        print(room_list[current_room].description)
        user_choice=input("What you want to do: ")
        user_choice.lower()
        if user_choice=="exit" or user_choice=="quit":
            break

        if user_choice=="north" or user_choice=="n":
            next_room=room_list[current_room].north
            if next_room==None:
                print("You can't go that way.")
            else :current_room=next_room
        #----------------------------------------------------------
        elif user_choice=="south" or user_choice=="s":
            next_room=room_list[current_room].south
            if next_room==None:
                print("You can't go that way.")
            else :current_room=next_room
        #----------------------------------------------------------
        elif user_choice=="east" or user_choice=="e":
            next_room=room_list[current_room].east
            if next_room==None:
                print("You can't go that way.")
            else :current_room=next_room
        #----------------------------------------------------------
        elif user_choice=="west" or user_choice=="w":
            next_room=room_list[current_room].west
            if next_room==None:
                print("You can't go that way.")
            else :current_room=next_room
        #----------------------------------------------------------
        else: print("I don't understand you.")
        
                      
    
main()    
    