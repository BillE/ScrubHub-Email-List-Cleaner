# ScrubHub-Email-List-Cleaner
use the results of a scrubbed email list to generate a clean list

steps:
1. read from original list with three fields: email, firstName, lastName
for each email address in original list, search for email address from scrubbed list
when we have a match, extract the result (we will use only 'Email Valid' here and ignore
both failures and uncertain results) and add full line from original list to new list

usage: python3 cleanEmailAddresses.py [originalFile] [scrubbedFile] [outputFile]

Used with Strike Iron's ScrubHub https://scrubhub.strikeiron.com
