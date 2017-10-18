from pathlib import Path
import os


def store_credentials_aws(profile,accesskey,secretkey):
    filename = str(Path.home()) + "/.aws/credentials"
    try:
        if "["+profile+"]" in open(filename).read():
            print("[+] The profile exists")
        else :
            print("[+] Creating profile in ~/.aws/credentials")
            with open(filename,'a') as f:
                f.write("\n")
                f.write("[" + profile + "]\n")
                f.write("aws_access_key_id=" + accesskey + "\n")
                f.write("aws_secret_access_key=" + secretkey + "\n\n")

    except FileNotFoundError:
        print("[+] Creating new configuration file...")
        print("[+] Storing AWS profile in ~/.aws/credentials......")
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'a') as f:
            f.write("["+profile+"]\n")
            f.write("aws_access_key_id=" + accesskey+"\n")
            f.write("aws_secret_access_key=" + secretkey)
        #  dev = boto3.Session(profile_name='default')


"""def update_credentials_aws(profile,accesskey,secretkey):
    filename = str(Path.home()) + "/.aws/credentials"
    try:
        if "[" + profile + "]" in open(filename).read():
            print("[+] The profile exists")
            print("[+] Updating...")
            with open(filename,'r') as f:
                for i,line in enumerate(f,1):
                    if "[" + profile + "]" in line:
                        replace=f.__next__()
                        replace1=f.__next__()

    except FileNotFoundError:
        print("[+] You must create a profile for updating")"""

