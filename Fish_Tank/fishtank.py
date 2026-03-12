# fishtank.py
# Fish Tank Monitor - Command Line Version
from os import system
import alkalinity
import calcium
import magnesium
import ph
import phosphate
import salinity
import temperature

class FishTankCLI():
    def __init__(self):
        print("Initialized FishTankCLI")

    def monitor(self):
        print("\nENVIRONMENTAL FACTORS:")
        print(ph.monitor())
        print(alkalinity.monitor())
        print(salinity.monitor())
        print(temperature.monitor())

        print("\nTRACE CHEMICALS:")
        print(calcium.monitor())
        print(magnesium.monitor())
        print(phosphate.monitor())


    def main(self):
        while True:
            print("\n=================================")
            print("      FISH TANK MONITOR")
            print("=================================")

            print("\nOptions:")
            print("1 - Perform Manual Check")
            print("2 - Show Help")
            print("3 - Exit")

            choice = input("\nEnter selection: ")
            system("clear")
            print("Message:")
            if choice == "1":
                self.monitor()

            elif choice == "2":
                print("This system monitors the health of a saltwater aquarium.")
                print("Environmental factors and chemical levels will be checked.")

            elif choice == "3":
                print("Exiting Fish Tank Monitor.")
                break

            else:
                print("Invalid selection. Try again.")