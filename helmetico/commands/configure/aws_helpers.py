import boto3
from pathlib import Path
import os


def store_credentials_aws(profile,accesskey,secretkey):
    filename = str(Path.home()) + "/.aws/credentials"
    try:
        if "["+profile+"]" in open(filename).read():
            print("the profile exists")
    except FileNotFoundError:
        print("No existe fichero... creado profile")
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            f.write("["+profile+"]\n")
            f.write("aws_access_key_id=" + accesskey+"\n")
            f.write("aws_secret_access_key=" + secretkey+"\n\n")
        #  dev = boto3.Session(profile_name='default')

def update_profile(profile):
    aws_credentials = Path("~/.aws/credentials")
    if aws_credentials.is_file():
        if profile in open("~/.aws/credentials").read():
            print("the profile exists")


