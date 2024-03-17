#!/usr/bin/python3

import os
import sys

pwd = os.getcwd()
input_name = sys.argv[1]
just_name = input_name.split(".")[0]


with open(f"{pwd}/{input_name}", "r") as f:
    lines = f.read().splitlines()

    for line in lines:
        line = line.lower()
        if "nproc" in line:
            nproc = line.split(" ")
            nproc = int(nproc[-1].strip())
            break
        else:
            nproc = 4 #DEFAULT
    
    for line in lines:
        line = line.lower()   
        
        if "%maxcore" in line:
            mem = line.split(" ")
            mem = mem[-1].strip()
            mem = int(mem)*int(nproc)/1000
            mem = str(int(mem))
            break
        else:
            mem="4" # DEFAULT

with open("submit-condor", "w") as output:
    output.write("Universe = vanilla\n")
    output.write("Requirements = HAS_GAUSSIAN_16 =?= True\n")
    output.write(f"Request_Cpus = {nproc}\n")
    output.write(f"Request_Memory = {mem}GB\n")
    output.write(f"Error = {just_name}.err\n")
    output.write("Should_Transfer_Files = Yes\n")
    output.write("When_To_Transfer_Output = ON_EXIT_OR_EVICT\n")
    output.write("Executable = /usr/local/bin/orca_submit\n")
    output.write("Transfer_Executable = True\n")
    output.write(f"Arguments = {input_name}\n")
    output.write(f"Transfer_Input_Files = {input_name}\n")
    output.write("\nQueue")

command = "condor_submit submit-condor"
os.system(command)
print(f"Job started with {nproc} CPUs and {mem} GB memory")
os.remove("submit-condor")

