# # # # Traffic signal controller: Simulate 3 cycles of a 4-way junction. 
# # # # Each direction gets green time based on a vehicle count entered by the user (under 10: 15s, 10-30: 30s, over 30: 45s).
# # # # Skip a direction with 0 vehicles, add a 5s yellow phase, and give priority to the direction with the highest count each cycle. 

# # # # In my understand of question :
# # # # we simulate 3 cycle yellow,green, red in a 4 way junction(4 side road)
# # # # all direction get green signal based on vehical count which is more vechiale that side will give a first priority . if vechial 10 means 15 sec and 10 to 30 means 30 sec over 30 upto 45 sec.
# # # #if vhecials is zero in any one of the way it skip (it means it ask again) add a 5sec yellow phase i did't get this. next give the pririty to heighest vechicals.
# # # # n = 3
# # # # i = 1
# # # # north = 4
# # # # south = 5
# # # # east = 1
# # # # weast = 0
# # # # while(n > i):
# # # #     if()





# # # # Get vehicle counts
# # # north = int(input("Enter North vehicles: "))
# # # east = int(input("Enter East vehicles: "))
# # # south = int(input("Enter South vehicles: "))
# # # west = int(input("Enter West vehicles: "))

# # # # 3 cycles
# # # for cycle in range(1, 4):

# # #     print("\nCycle:", cycle)

# # #     # Find highest vehicle count
# # #     highest = north

# # #     if east > highest:
# # #         highest = east

# # #     if south > highest:
# # #         highest = south

# # #     if west > highest:
# # #         highest = west

# # #     # Priority direction
# # #     if highest == north and north != 0:
# # #         print("North has priority")
# # #     elif highest == east and east != 0:
# # #         print("East has priority")
# # #     elif highest == south and south != 0:
# # #         print("South has priority")
# # #     elif highest == west and west != 0:
# # #         print("West has priority")

# # #     # North
# # #     if north == 0:
# # #         print("North → SKIP")
# # #     elif north < 10:
# # #         print("North → GREEN 15 seconds → YELLOW 5 seconds")
# # #     elif north <= 30:
# # #         print("North → GREEN 30 seconds → YELLOW 5 seconds")
# # #     else:
# # #         print("North → GREEN 45 seconds → YELLOW 5 seconds")

# # #     # East
# # #     if east == 0:
# # #         print("East → SKIP")
# # #     elif east < 10:
# # #         print("East → GREEN 15 seconds → YELLOW 5 seconds")
# # #     elif east <= 30:
# # #         print("East → GREEN 30 seconds → YELLOW 5 seconds")
# # #     else:
# # #         print("East → GREEN 45 seconds → YELLOW 5 seconds")

# # #     # South
# # #     if south == 0:
# # #         print("South → SKIP")
# # #     elif south < 10:
# # #         print("South → GREEN 15 seconds → YELLOW 5 seconds")
# # #     elif south <= 30:
# # #         print("South → GREEN 30 seconds → YELLOW 5 seconds")
# # #     else:
# # #         print("South → GREEN 45 seconds → YELLOW 5 seconds")

# # #     # West
# # #     if west == 0:
# # #         print("West → SKIP")
# # #     elif west < 10:
# # #         print("West → GREEN 15 seconds → YELLOW 5 seconds")
# # #     elif west <= 30:
# # #         print("West → GREEN 30 seconds → YELLOW 5 seconds")
# # #     else:
# # #         print("West → GREEN 45 seconds → YELLOW 5 seconds")
# # north = int(input("Enter North vehicles: "))
# # east = int(input("Enter East vehicles: "))
# # south = int(input("Enter South vehicles: "))
# # west = int(input("Enter West vehicles: "))

# # for cycle in range(1, 4):

# #     print("\nCycle:", cycle)

# #     # Find highest vehicle count
# #     highest = north

# #     if east > highest:
# #         highest = east

# #     if south > highest:
# #         highest = south

# #     if west > highest:
# #         highest = west

# #     # Highest priority direction
# #     if highest == north and north != 0:
# #         print("North has priority")

# #         print("North → GREEN")
# #         if north < 10:
# #             print("Green time: 15 seconds")
# #         elif north <= 30:
# #             print("Green time: 30 seconds")
# #         else:
# #             print("Green time: 45 seconds")
# #         print("North → YELLOW 5 seconds")

# #     elif highest == east and east != 0:
# #         print("East has priority")

# #         print("East → GREEN")
# #         if east < 10:
# #             print("Green time: 15 seconds")
# #         elif east <= 30:
# #             print("Green time: 30 seconds")
# #         else:
# #             print("Green time: 45 seconds")
# #         print("East → YELLOW 5 seconds")

# #     elif highest == south and south != 0:
# #         print("South has priority")

# #         print("South → GREEN")
# #         if south < 10:
# #             print("Green time: 15 seconds")
# #         elif south <= 30:
# #             print("Green time: 30 seconds")
# #         else:
# #             print("Green time: 45 seconds")
# #         print("South → YELLOW 5 seconds")

# #     elif highest == west and west != 0:
# #         print("West has priority")

# #         print("West → GREEN")
# #         if west < 10:
# #             print("Green time: 15 seconds")
# #         elif west <= 30:
# #             print("Green time: 30 seconds")
# #         else:
# #             print("Green time: 45 seconds")
# #         print("West → YELLOW 5 seconds")

# # Input
# north = int(input("Enter North vehicles: "))
# east = int(input("Enter East vehicles: "))
# south = int(input("Enter South vehicles: "))
# west = int(input("Enter West vehicles: "))

# # 3 cycles
# for cycle in range(1, 4):

#     print("\nCycle", cycle)

#     # Find highest vehicle count
#     highest = north

#     if east > highest:
#         highest = east

#     if south > highest:
#         highest = south

#     if west > highest:
#         highest = west

#     # -------------------------
#     # Priority direction
#     # -------------------------

#     if highest == north and north != 0:
#         print("North → GREEN")

#         if north < 10:
#             print("Green: 15 seconds")
#         elif north <= 30:
#             print("Green: 30 seconds")
#         else:
#             print("Green: 45 seconds")

#         print("North → YELLOW 5 seconds")

#     elif highest == east and east != 0:
#         print("East → GREEN")

#         if east < 10:
#             print("Green: 15 seconds")
#         elif east <= 30:
#             print("Green: 30 seconds")
#         else:
#             print("Green: 45 seconds")

#         print("East → YELLOW 5 seconds")

#     elif highest == south and south != 0:
#         print("South → GREEN")

#         if south < 10:
#             print("Green: 15 seconds")
#         elif south <= 30:
#             print("Green: 30 seconds")
#         else:
#             print("Green: 45 seconds")

#         print("South → YELLOW 5 seconds")

#     elif highest == west and west != 0:
#         print("West → GREEN")

#         if west < 10:
#             print("Green: 15 seconds")
#         elif west <= 30:
#             print("Green: 30 seconds")
#         else:
#             print("Green: 45 seconds")

#         print("West → YELLOW 5 seconds")

#     # -------------------------
#     # Remaining directions
#     # -------------------------

#     if north != highest:

#         if north == 0:
#             print("North → SKIP")
#         elif north < 10:
#             print("North → GREEN 15 seconds → YELLOW 5 seconds")
#         elif north <= 30:
#             print("North → GREEN 30 seconds → YELLOW 5 seconds")
#         else:
#             print("North → GREEN 45 seconds → YELLOW 5 seconds")

#     if east != highest:

#         if east == 0:
#             print("East → SKIP")
#         elif east < 10:
#             print("East → GREEN 15 seconds → YELLOW 5 seconds")
#         elif east <= 30:
#             print("East → GREEN 30 seconds → YELLOW 5 seconds")
#         else:
#             print("East → GREEN 45 seconds → YELLOW 5 seconds")

#     if south != highest:

#         if south == 0:
#             print("South → SKIP")
#         elif south < 10:
#             print("South → GREEN 15 seconds → YELLOW 5 seconds")
#         elif south <= 30:
#             print("South → GREEN 30 seconds → YELLOW 5 seconds")
#         else:
#             print("South → GREEN 45 seconds → YELLOW 5 seconds")

#     if west != highest:

#         if west == 0:
#             print("West → SKIP")
#         elif west < 10:
#             print("West → GREEN 15 seconds → YELLOW 5 seconds")
#         elif west <= 30:
#             print("West → GREEN 30 seconds → YELLOW 5 seconds")
#         else:
#             print("West → GREEN 45 seconds → YELLOW 5 seconds")



north = 10
weast = 5
south = 1
east = 15
h1 = 0
h2 = 0
h3 = 0
h4 = 0
for i in range(1,):
    if(north > weast and north > south  and north > east):
        print("North is h1",north)
    elif(south > weast and south > north  and south > east):
        print("south is h1",south)
    elif(east > weast and east > south  and east > north):
        print("east is h1",east)
    elif(weast > north and weast > south  and weast > east):
        print("weast is h1",weast)  