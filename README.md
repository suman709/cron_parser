# cron_parser

Problem statement: Write a command line application or script which parses a cron string and expands each field to show the times at which it will run.

INPUT: your-program  "*/15 0 1,15 * 1-5" /usr/bin/find

OUTPUT: 
minute 0 15 30 45
hour 0
day of month 1 15
month 1 2 3 4 5 6 7 8 9 10 11 12
day of week 1 2 3 4 5
command /usr/bin/find


Tech_Used: python
Have used croniter library of python (check requirements file)


Command line input: python main.py "*/15 0 1,15 * 1-5" /usr/bin/find
