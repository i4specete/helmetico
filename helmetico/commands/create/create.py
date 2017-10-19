from pathlib import Path
import os,json
from helmetico.commons.helmetico_helpers import *

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

def create_iam_aws(profile,user,group):
    if check_profile(profile):
        print("existe")
        if user is not None:
            print(user)
