#! /usr/bin/python
#-*- coding: utf-8 -*-

import string
import sys
import secrets
from workflow import Workflow3

def gen_passwd():
    res = []
    # letter dectionary
    # alphabet = string.ascii_letters + string.digits + string.punctuation
    
    # Random a passwd， Contains only letters and numbers, length 16
    passwd_length = 16
    while True:
        passwd = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(passwd_length))
        if (any(c.islower() for c in passwd)
                and any(c.isupper() for c in passwd)
                and sum(c.isdigit() for c in passwd) >= 3):
            break
    
    res.append(passwd)

    # Random a passwd, Contain letters and numbers, special characters, length 16
    passwd_length = 16
    while True:
        passwd = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(passwd_length))
        if (any(c.islower() for c in passwd)
                and any(c.isupper() for c in passwd)
                and sum(c.isdigit() for c in passwd) >= 3):
            break

    res.append(passwd)

    return res

def generate_feedback_results(wf):
    result = gen_passwd()

    res = {
                'title': result[0],
                'subtitle': '' ,
                "valid": True,
                'arg': result
            }
    wf.add_item(**res)
    res = {
                'title': result[1],
                'subtitle': '' ,
                "valid": True,
                'arg': result
            }
    wf.add_item(**res)
    wf.send_feedback()

def main():
    wf = Workflow3()
    generate_feedback_results(wf)

if __name__ == "__main__":
    main()