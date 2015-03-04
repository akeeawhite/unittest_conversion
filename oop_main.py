__author__ = 'Akeea'
"""
This program is to display a menu of conversion choices for the user.
These choices include:
Press 1 to convert Kilometers to Miles
Press 2 to convert Meters to Yards
Press 3 to convert centimeters to inches
Press 4 to quit
"""

#Calculations class that calculates the numbers inputed by the user
class Calculations:
    #conversion from kilometers to miles
    def conversionKilo(self, k):
        self.miles = k * .625
        return self.miles

    #conversion from meters to yards
    def conversionMeters(self, m):
        self.yards = 1.0936 * m
        return self.yards

    #conversion from centimeters to inches
    def conversionCenti(self, cent):
        self.inches = cent * .39
        return self.inches

    #display's the goodbye message
    #def goodbye(self):
        #print("thank you for using the conversion program, have a nice day.")
    #return self.goodbye

#Class for getting the input from the users
class getInput:

        self = Calculations()
        while True:
            userinput = input("Press 1 for centimeters to inches, Press 2 for meters to yards,"
                              "\n Press 3 for kilometers to miles, or Press 4 to quit:")
            if userinput == '4':
                #self.goodbye
                print("thank you for using the conversion program, have a nice day.")
                break

            elif userinput == '1':
                centimeters = int(input("Enter the number of centimeters that you would like to convert to inches:"))
                i = self.conversionCenti(centimeters)
                print(i, "inches")

            elif userinput == '2':
                meters = int(input("Enter the number of meters that you would like to convert to yards:"))
                y = self.conversionMeters(meters)
                print(y, "yards")

            elif userinput == '3':
                kilometers = int(input("Enter the number of kilometers that you would like to convert to miles:"))
                mi = self.conversionKilo(kilometers)
                print(mi, "miles")

            else:
                    print("User input error, please restart \nthe input must be 1, 2, 3, or 4.")




