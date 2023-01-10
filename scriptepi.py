import subprocess
import time

script_list = ["epi1.py", "epi2.py", "epi3.py", "epi4.py", "epi5.py", "epi6.py", "epi7.py", "epi8.py", "epi9.py", "epi10.py"]

for script in script_list:
    subprocess.run(["python", script])
    time.sleep(2)