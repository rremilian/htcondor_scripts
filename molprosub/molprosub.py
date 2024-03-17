#!/usr/bin/python3

import os
import argparse
import math

pwd = os.getcwd()

parser = argparse.ArgumentParser(
    prog="Molpro Submitter"
)

parser.add_argument("inputfile", type=str, help="Input file name")
parser.add_argument("-m", "--memory", type=int, help = "Memory allocation in MW per core (125 MW = 1 GB)", default=125)
parser.add_argument("-n", "--nproc", type=int, help = "Number of CPUs to allocate for the job", default=1)
args = parser.parse_args()
just_name = args.inputfile.split(".")[0]

with open("submit-condor", "w") as output:
    output.write("Universe = vanilla\n")
    output.write("Requirements = HAS_MOLPRO =?= True\n")
    output.write(f"Request_Cpus = {args.nproc}\n")
    output.write(f"Request_Memory = {math.ceil(args.memory/125)}GB\n")
    output.write(f"Error = {just_name}.err\n")
    output.write("Should_Transfer_Files = Yes\n")
    output.write("When_To_Transfer_Output = ON_EXIT_OR_EVICT\n")
    output.write(f"Executable = /usr/local/bin/molpro_submit\n")
    output.write("Transfer_Executable = True\n")
    output.write(f"Arguments = {args.nproc} {args.memory} {args.inputfile}\n")
    output.write(f"Transfer_Input_Files = {args.inputfile}\n")
    output.write("\nQueue")

command = "condor_submit submit-condor"
os.system(command)
print(f"Job started with {args.nproc} CPUs and {math.ceil(args.memory/125)}GB memory per core")
