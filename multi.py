import json
import subprocess

with open("config.json") as fp:
    config = json.load(fp)

range_num = config["range"]["max"] - config["range"]["min"]
count = int(input("process count: "))
per = int(range_num / count)
processes = []

for n in range(count):
    r = [
        config["range"]["min"] + (per * n),
        config["range"]["min"] + (per * (n + 1))
    ]
    p = subprocess.Popen(["python", "scraper", str(r[0]), str(r[1])])
    processes.append(p)