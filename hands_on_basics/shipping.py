# Shipping possibility calculation

# N = Number of trips
# P = Number of containers to be transported in each trip
# M = Number of boats for transporting containers
# C = Boat capacity in terms of Containers


def shipping_possible(input1, input2):
    try:
        trip_numbers = [int(i) for i in input1.split(" ")]
        containers_per_trip = [int(i) for i in input2.split(" ")]
        print("Trip Numbers(N C M) : %s" % trip_numbers)
        print(f"Containers per trip : {containers_per_trip}")
        print(f"Per trip container capacity(C X M) : {trip_numbers[1] * trip_numbers[2]}")

        for i in trip_numbers:
            if i < 1 or i > 100:
                print(f"{i} is invalid input for trip numbers")
                return

        if trip_numbers[0] != len(containers_per_trip):
            print("Invalid input! Provided container capacities count do not match the number of trips")
            return

        possible = True
        for c in containers_per_trip:
            if c > trip_numbers[1] * trip_numbers[2]:
                print(f"No, {c} is more than the per trip container capacity!")
                possible = False
                break

        if possible:
            print("Yes")

    except Exception as e:
        print("Error processing your request.", e)


def shipping_problem():
    input1 = input("Enter N(Number of trips) [SPACE] C(Boat capacity in # of containers) [SPACE] M(Total number of "
                   "Boats) : ")
    input2 = input("P(Number of containers for each trip) [SPACE] Separated : ")
    shipping_possible(input1, input2)


print(__name__)

if __name__ == "__main__":
    shipping_problem()