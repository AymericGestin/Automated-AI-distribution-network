import os
import subprocess
path=os.path.dirname(os.path.dirname(__file__))
ligne1="docker run -it -v "+path+":/root/projects/benchmarks lapkt/lapkt-public "
ligne2="./siw --domain /root/projects/benchmarks/CSV_Problem/domainv8.pddl --problem /root/projects/benchmarks/CSV_Problem/disnet001v5.pddl\n"
ligne3="cp /root/projects/lapkt/compiled_planners/plan.ipc /root/projects/benchmarks/Plan/plan.txt\n"
ligne4="exit"
command=ligne1+ligne2
print(command)
#subprocess.Popen(command)
os.system(command)
