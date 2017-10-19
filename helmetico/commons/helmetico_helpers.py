from pathlib import Path
import json

def check_profile(profile):
    filename = str(Path.home()) + "/.helmetico/credentials.json"
    noexist=True
    try:
        with open(filename) as json_file:
            data = json.load(json_file)
            for i in data['profiles']:
                if profile in i['profile']:
                    print("[+] OK! This profile exists.")
                    noexist = False
                    return True
            if noexist:
                print("[+] This profile doesn't exist")
                return False
    except FileNotFoundError:
        print("[+] First of all, you must create a helmetico profile \"helmetico create credentials\" ")
        return False