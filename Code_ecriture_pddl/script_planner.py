import os
import subprocess
path=os.path.dirname(os.path.dirname(__file__))
ligne1="docker run --name test -it -d --rm -v "+path+":/root/projects/benchmarks lapkt/lapkt-public &&"
ligne2="docker exec -it test ./dfs_plus --domain /root/projects/benchmarks/CSV_Problem/domainv8.pddl --problem /root/projects/benchmarks/CSV_Problem/problem_16.pddl &&"
ligne3="docker exec -it test cp /root/projects/lapkt/compiled_planners/plan.ipc /root/projects/benchmarks/Plan/plan_16.txt &&"
ligne4="docker kill test"
command=ligne1+ligne2+ligne3+ligne4
#subprocess.Popen(command)
os.system(command)
