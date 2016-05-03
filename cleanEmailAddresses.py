# use the results of a scrubbed email list to generate a clean list
#
# steps:
# 1. read from original list with three fields: email, firstName, lastName
# for each email address in original list, search for email address from scrubbed list
# when we have a match, extract the result (we will use only 'Email Valid' here and ignore
# both failures and uncertain results) and add full line from original list to new list
#
# usage: python3 cleanEmailAddresses.py [originalFile] [scrubbedFile] [outputFile]
#
# Used with Strike Iron's ScrubHub https://scrubhub.strikeiron.com


import csv, sys, os, argparse

# Scrub Hub uses two different tags for this, infuriatingly
VALID_EMAIL_TAG = "Email Valid"
VALID_EMAIL_TAG_2 = "Valid"

# valid email addresses to check against original list
cleanEmails = []

# parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("original")
parser.add_argument("scrubbed")
parser.add_argument("output")
args = parser.parse_args()

originalFile = args.original
scrubbedFile = args.scrubbed
cleanedFile = args.output

# HELPER METHODS #
def exitWithUsageError(self, errorMsg):
    print(errorMsg)
    sys.exit("usage: python3 cleanEmailAddresses.py [originalFile] [scrubbedFile] [outputFile]");

# MAIN #

# open scrubbed file and put all scrubbed emails into an array
if os.path.exists(scrubbedFile):
    try:
        dictReader = csv.DictReader(open(scrubbedFile, 'r'), fieldnames = ['email', 'resultCode', 'resultText'],
                                    delimiter = ',', quotechar = '"')

        for row in dictReader:
            if row['resultText'] == VALID_EMAIL_TAG or row['resultText'] == VALID_EMAIL_TAG_2:
                cleanEmails.append(row['email'])

        cleanEmailCount = str(len(cleanEmails))
    except:
        exitWithUsageError("Could not read file: " + scrubbedFile)
else:
    exitWithUsageError("Could not read file: " + scrubbedFile)

# get count of original records
if os.path.exists(originalFile):
    try:
        ofHandle = open(originalFile, 'r')
        originalEmailCount = sum(1 for _ in ofHandle)
        ofHandle.close()
    except:
        exitWithUsageError("Could not read file: " + scrubbedFile)
else:
    exitWithUsageError("Could not read file: " + scrubbedFile)

# This is based on a fixed file format of lastName, firstName, email
dictReader = csv.DictReader(open(originalFile, 'r'), fieldnames = ['lastName', 'firstName', 'email'],
                        delimiter = ',', quotechar = '"')

# Read records from original file, if the email address exists in the cleaned list, write it to the out file

fOut = open(cleanedFile,'w')

# for each cleaned email addresses, write full row from original file to output file
for row in dictReader:
    if row['email'] in cleanEmails:
        fOut.write(row['lastName'] + ',' + row['firstName'] + ',' + row['email'] + '\n')

fOut.close()

# print summary and exit
sys.exit("Found " + str(cleanEmailCount) + " clean email addresses out of " + str(originalEmailCount))