from pathlib import Path
import os,json


def update_credentials_aws(profile,accesskey,secretkey):
    filename = str(Path.home()) + "/.helmetico/credentials.json"
    noexist = True
    try:
        with open(filename) as json_file:
            data = json.load(json_file)
            for i in data['profiles']:
                if profile in i['profile']:
                    print("[+] Updating "+profile+" profile....")
                    i['accesskey']=accesskey
                    i['secretkey']=secretkey
                    print("[+] DONE!")
                    noexist=False
            if noexist:
                print("[+] You need to create a profile with \"helmetico create credentials\"")
        with open(filename, 'w') as f:
                json.dump(data, f)

    except FileNotFoundError:
        print("[+] You need to create a profile with \"helmetico create credentials\"")

