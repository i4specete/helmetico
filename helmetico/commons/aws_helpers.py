from pathlib import Path
import os,json


def store_credentials_aws(profile,accesskey,secretkey):
    filename = str(Path.home()) + "/.helmetico/credentials.json"
    noexist=True
    try:
        with open(filename) as json_file:
            data = json.load(json_file)
            for i in data['profiles']:
                if profile in i['profile']:
                    print("[+] This profile exists currently")
                    noexist=False
            if noexist:
                print("[+] Adding new "+profile+" profile .....")
                data['profiles'].append({
                'profile':profile,
                'accesskey':accesskey,
                'secretkey':secretkey})

        with open(filename, 'w') as f:
            json.dump(data,f)


    except FileNotFoundError:
        print("[+] Creating new configuration file...")
        print("[+] Storing AWS profile in "+filename+ " ......")
        data = {}
        data['profiles'] = []
        data['profiles'].append({
            'profile':profile,
            'accesskey':accesskey,
            'secretkey':secretkey})

        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w') as f:
            json.dump(data,f)

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


def delete_credentials_aws(profile):
    filename = str(Path.home()) + "/.helmetico/credentials.json"
    noexist = True
    count = 0

    try:
        with open(filename) as json_file:
            data = json.load(json_file)
            for i in data['profiles']:
                if profile in i['profile']:
                    print("[+] Deleting "+profile+" profile....")
                    del data['profiles'][count]
                    print("[+] DONE!")
                    noexist=False
                count=count+1
            if noexist:
                print("[+] You need to create a profile with \"helmetico create credentials\"")
        with open(filename, 'w') as f:
                json.dump(data, f)

    except FileNotFoundError:
        print("[+] You need to create a profile with \"helmetico create credentials\"")



