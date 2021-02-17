# Author David
# lab.5.1.tuple.py
# The program creates a tuple that stroes the months of the year
# From the first tuple a second tuple is created with the summer months
# (May, June, July), print out the summer months one at a time

months = ("January",
            "Feburary",
            "March",
            "April",
            "May",
            "June",
            "july",
            "August",
            "September",
            "October",
            "November",
            "December"
)
summer = months[4:7]
for month in summer:
    print(month)