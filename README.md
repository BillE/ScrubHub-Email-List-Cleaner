# ScrubHub-Email-List-Cleaner
Uses the results of a scrubbed email list to generate a clean list of records in csv format.

Reads from original list with three fields: email, firstName, lastName.
For each record in original list, searches for email address from scrubbed list.
When a match is found, extracts the result and adds full line from original list to new list

Currently, StrikeIron uses two result codes to indicate a valid email: 'Email Valid' and 'Valid'.
We use only these status codes, ignoring any vague results.

usage: python3 cleanEmailAddresses.py [originalFile] [scrubbedFile] [outputFile]

Used with Strike Iron's ScrubHub https://scrubhub.strikeiron.com
