import math


# function takes a start time, duration time and optional day of week returns the new time and if any days passed
def add_time(start, duration, dayOfWeek=""):
    # split start time into list
    startList = start.split()

    # get time components, timeOfDay, list[hour,minutes]
    timeOfDay = startList[1]
    startTimeComponents = timeStringToList(startList[0])
    durationComponents = timeStringToList(duration)

    durationComponents[1] = durationComponents[1] + startTimeComponents[1]

    startTimeComponents = minutesToHours(startTimeComponents)
    durationComponents = minutesToHours(durationComponents)

    newHour = startTimeComponents[0]
    newMin = durationComponents[1]

    daysPassed = 0

    while durationComponents[0] > 0:
        if newHour < 12:
            newHour = newHour + 1
            if newHour == 12:
                timeOfDay = changeTimeOfDay(timeOfDay)
                daysPassed = daysPassed + (1 if timeOfDay == "AM" else 0)
        else:
            newHour = 1

        durationComponents[0] = durationComponents[0] - 1

    if len(dayOfWeek) > 0:
        dayOfWeek = advanceWeekDays(dayOfWeek, daysPassed)

    daysPassed = daysPassedToString(daysPassed)

    return str(newHour) + ":" + str(newMin).zfill(2) + " " + timeOfDay + dayOfWeek + daysPassed


# toggle am/pm depending on passed in time of day
def changeTimeOfDay(timeOfDay):
    return "AM" if timeOfDay == "PM" else "PM"


# takes time list [hour:min] and splits to list, converts elements to int
def timeStringToList(time):
    return [int(i) for i in (time.split(":"))]


# function takes time and converts to hour : 59 min max format
def minutesToHours(time):
    while time[1] >= 60:
        time[0] = time[0] + 1
        time[1] = time[1] - 60

    return time


# function takes current day of week and days passed variable and returns current week day
def advanceWeekDays(dayOfWeek, daysPassed):
    weekdays = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday")
    currentIndex = weekdays.index(dayOfWeek.lower())

    for count in range(daysPassed):
        if currentIndex == 6:
            currentIndex = 0
        else:
            currentIndex = currentIndex + 1

    return ", " + weekdays[currentIndex].capitalize()


# takes days passed and returns string
def daysPassedToString(daysPassed):
    numberOfDays = ""

    if daysPassed > 0:
        numberOfDays = " (next day)" if daysPassed == 1 else (" (" + str(daysPassed) + " days later)")

    return numberOfDays
