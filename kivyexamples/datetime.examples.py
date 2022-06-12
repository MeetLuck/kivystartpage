from datetime import datetime
# NOTE string -> datetime => datetime.strptime(string, format)
# NOTE datetime -> string => datetime.strftime(format)

# ---------------------- strftime --------------------------------------
'''
%d 	Day of month as 01,02
%m 	Months as 01,02
%y 	Year without century as 11,12,13
%Y 	Year with century 2011,2012
%H 	24 Hours clock from 00 to 23
%p 	AM, PM
%M 	Minutes from 00 to 59
%S 	Seconds from 00 to 59
'''

# ----------------------- strptime -----------------------------------------
'''
%d 	Day of month as 01,02
%-d Day of the month as 1,2
%m 	Months as 01,02
%-m Month as 1, 2, ..., 12
%y 	Year without century as 11,12,13
%-y Year without century as a decimal number.  0, 1, 2
%Y 	Year with century 2011,2012
%H 	24 Hours clock from 00 to 23
%M 	Minutes from 00 to 59
%S 	Seconds from 00 to 59
'''

datetime_date1 = datetime.strptime("09/23/2022 8:28","%m/%d/%Y %H:%M")
string_date1   = datetime_date1.strftime("%Y-%m-%d %H:%M:%S")
print(datetime_date1, type(datetime_date1))
print(string_date1, type(string_date1))

date = datetime(2022,6,1)
print(date, type(date))
