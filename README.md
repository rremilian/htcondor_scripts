# HTCondor Submission Scripts

## **g16sub**
<p align="justify">Automation script used for the submission of a Gaussian Job File (GJF) to a cluster that uses HTCondor workload management system. The script takes as an argument the GJF and retrieves from it the number of cores and the amount of memory that must be allocated to the job. If the GJF does not have any information regarding the number of cores or the necessary amount of memory, the script will allocate by default 4 cores and 4 GB of memory. The script is configured for Gaussian 16. The user should modify the <i>g16_submit</i> file with the correct paths for the Gaussian 16 binaries and the scratch directory.</p>

<b>Example:</b>

<code>g16sub input.gjf</code>

## **orcasub**
<p align="justify">Automation script used for the submission of ORCA input files to a cluster that uses HTCondor workload management system. The script takes as an argument the input file and retrieves from it the number of cores and the amount of memory that must be allocated to the job. If the input file does not have any information regarding the number of cores or the necessary amount of memory, the script will allocate by default 4 cores and 4 GB of memory per core. The user should modify the <i>orca_submit</i> file with the correct paths for the ORCA binaries, and MPI libraries and binaries. 
<b>Example:</b>

<code>orcasub input.inp</code>

## **molprosub**
<p align="justify">Automation script used for the submission of Molpro input file to a cluster that uses HTCondor workload management system. The script takes three arguments: the number of cores (<i>-n</i>) that must be allocated to the job, the amount of memory (<i>-m</i>) that must be allocated to the job (in <i>megawords</i> (MW)) and the name of the input file. By default, the value for the number of CPUs is set to 1 and the amount of memory is set to 125 MW (1 GB). The user should modify the <i>molpro_submit</i> file with the correct paths for the Molpro program and the scratch directory.</p>

<b>Example:</b>

<code>molprosub -n 12 -m 1250 input.inp</code>

This command will allocate 12 CPUs and 1250 MW (10 GB) of memory for the job and will submit it to the queue.

