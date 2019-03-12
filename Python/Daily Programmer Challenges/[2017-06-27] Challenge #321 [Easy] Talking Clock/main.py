'''
Description

No more hiding from your alarm clock! You've decided you want your computer to keep you updated on the time so you're never late again. A talking clock takes a 24-hour time and translates it into words.

Input Description

An hour (0-23) followed by a colon followed by the minute (0-59).

Output Description

The time in words, using 12-hour format followed by am or pm.

Sample Input data

00:00
01:30
12:05
14:01
20:29
21:00

Sample Output data

It's twelve am
It's one thirty am
It's twelve oh five pm
It's two oh one pm
It's eight twenty nine pm
It's nine pm

Extension challenges (optional)

Use the audio clips found here to give your clock a voice.
'''
from datetime import datetime
# Getting time and date
time = str(datetime.now())
# putting only needed parts of time in strings
hour = time[11:13]
ten = time[14]
single = time[15]
# Converting Strings to int to do math
hour = int(hour)
ten = int(ten)
single = int(single)
print()
# Default value of the half of day
half = "am"
# Lists of the words for output
hour_out = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]
tens_out = ["oh ", "", "twenty ", "thirty ", "fourty ", "fifty "]
teens_out = ["ten", "eleven ", "twelve ", "thirteen ", "fourteen ",
             "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]
# Converting to 12 hour time and checking if its the afternoon
if hour > 12:
    hour = hour - 12
    half = "pm"
# Outputing the time
if ten == 0 and single == 0:
    print("The time is", hour_out[hour], half)
elif ten == 1:
    print("The time is", hour_out[hour], teens_out[ten], half)
else:
    print("The time is", hour_out[hour - 1], tens_out[ten], hour_out[single - 1])

