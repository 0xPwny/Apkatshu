import argparse
import os
import time
"""                                                     This tool is used to gather information from decompiled
apks the information that gets collected is:
emails
APIs
links
and many more in the future
"""                                                                                                             parser = argparse.ArgumentParser()
parser.add_argument("--dir", help="directory to decompil
ed apk")
args = parser.parse_args()
def search_domain():
    print("[x] Grabbing Domains..")
    time.sleep(7)
    urlfile = "domain.txt"

    """
    searches for .com domains
    """
    os.system("grep -r 'http://' * > domain.txt")
    print("[x] Sorting the domains")
    time.sleep(4)
    with open(urlfile,"r") as domain:
        for domains in domain:
            if "http://" in domains:
                print(domains)
def search_email():
    emailfile = "email.txt"
    """
    searches for emails
    """
    print("[x] Grabbing Emails")
    time.sleep(7)
    os.system("grep -r '@' * > email.txt")
    print("[x] Sorting the emails")
    time.sleep(4)
    with open(emailfile,"r") as email:
        for emails in email:
            if "@gmail" or "@" in emails:
                print(emails)

if args.dir:
    os.chdir(args.dir)
    search_domain()
    search_email()
