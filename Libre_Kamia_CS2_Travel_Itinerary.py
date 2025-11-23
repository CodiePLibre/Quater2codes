destinations = []
print("Enter your 5 destinations:")
for i in range(5):
    place = input("Destination " + str(i+1) + ": ")
    destinations.append(place)
    
print("Original Travel Itinerary:")
for i in range(5):
    print(str(i+1) + ". " + destinations[i])

print("Lets update your 2nd and 5th destinations.")
destinations[1] = input("Enter a new destination for position 2: ")
destinations[4] = input("Enter a new destination for position 5: ")

print("Updated Travel Itinerary:")
for i in range(5):
    print(str(i+1) + ". " + destinations[i])
