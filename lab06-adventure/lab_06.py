class Room:
    def __init__(self,description, north, south, east,west):
        self.description=description 
        self.north=north
        self.east =east
        self.south=south
        self.west=west
def main():
    room_list=[]
    room=Room("Bedroom2",1,None,1,None)
    room_list.append(room)
    room=Room("Bedroom1",None,1,1,None)
    room_list.append(room)
    room=Room("North Hall",1,1,1,1)
    room_list.append(room)
    room=Room("South Hall",1,None,1,1)
    room_list.append(room)
    room=Room("kitchen",None,1,1,1)
    room_list.append(room)
    room=Room("Diving Room",1,None,None,1)
    room_list.append(room)
    room=Room("Balcony",None,1,1,1)
    room_list.append(room)
    current_room=0
    print(room_list[current_room].description)
    done=False
    while (done==False):
        print("")
        print(room_list[current_room].description)
        user_choice=input("What you want to do: ")
        user_choice.lower()
        if user_choice=="north" or user_choice=="n":
            next_room=room_list[current_room].north
            if next_room==None:
                print("You can't go that way.")
            else :current_room=next_room
            
    
main()    
    