import requests
import sys
import os
from dotenv import load_dotenv

if len(sys.argv) != 2:
    print('Wrong number of arguments')
    exit(0)


load_dotenv()
cookie = os.getenv("COOKIE")
day = int(sys.argv[1])
headers = {'session': cookie}
url = f'https://adventofcode.com/2021/day/{day}/input'

session = requests.Session()
resp = session.get(url, cookies=headers)

with os.scandir(os.getcwd()) as it:
    for entry in it:
        if entry.name.startswith(f'{day}') and entry.is_dir:
            problem_folder = entry.name

filename = 'input.txt'
current_path = os.getcwd()
full_path = os.path.join(current_path, problem_folder, filename)


in_file = open(full_path, 'w')
in_file.write(resp.text)
in_file.close()
