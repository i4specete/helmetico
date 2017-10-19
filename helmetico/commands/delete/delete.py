from pathlib import Path
import json

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



