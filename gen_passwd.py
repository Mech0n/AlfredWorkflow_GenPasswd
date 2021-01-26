#! /usr/bin/python
#-*- coding: utf-8 -*-

import string
import sys
import secrets
from workflow import Workflow3

def gen_passwd():
    # letter dectionary
    alphabet = string.ascii_letters + string.digits

    # set passwd length
    passwd_length = 16
    
    # random a passwd
    while True:
        passwd = ''.join(secrets.choice(alphabet) for i in range(passwd_length))
        if (any(c.islower() for c in passwd)
                and any(c.isupper() for c in passwd)
                and sum(c.isdigit() for c in passwd) >= 3):
            break

    return passwd

def generate_feedback_results(result):
    wf = Workflow3()
    kwargs = {
                'title': result,
                'subtitle': '' ,
                "valid": True,
                'arg': result
            }
    wf.add_item(**kwargs)
    wf.send_feedback()

def main():
    query_data = gen_passwd()
    generate_feedback_results(query_data)

if __name__ == "__main__":
    main()