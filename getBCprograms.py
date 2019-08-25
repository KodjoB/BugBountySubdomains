import os
import sys
import requests
import json
import tldextract

programs = []

def getHTML(url):

        headers = {"X-Requested-With":"XMLHttpRequest", "accept": "application/json"}
        html = requests.get(url, headers=headers)
        safe_html = (html.text).encode('cp850',errors='replace')
        return (safe_html)


def getPrograms():
        for x in range(0,5):
            offset = [0,25,50,75,100,125]
            res = getHTML("https://bugcrowd.com/programs.json?points_only[]=false&sort[]=promoted-desc&offset[]="+str(offset[x]))
            split = res.split(",")
            #jhtml = json.loads(safe_html)
            for parts in split:
                if '"program_url"' in parts:
                    if 'ynab' not in parts:
                        programs.append((parts).split(":")[1].strip('"'))


if __name__ == "__main__":
    getPrograms()
    for program in programs:
        print (program.strip("/"))
