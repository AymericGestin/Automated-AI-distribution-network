import os
import subprocess
path=os.path.dirname(os.path.dirname(__file__))
def run_planner(Numero_Reseau,methode="dfs_plus",domain="domainv8.pddl"):
    ligne1="docker run --name test -it -d --rm -v "+path+":/root/projects/benchmarks lapkt/lapkt-public &&"
    ligne2="docker exec -it test ./"+methode+" --domain /root/projects/benchmarks/CSV_Problem/"+domain+" --problem /root/projects/benchmarks/CSV_Problem/problem_"+str(Numero_Reseau)+".pddl &&"
    ligne3="docker exec -it test cp /root/projects/lapkt/compiled_planners/plan.ipc /root/projects/benchmarks/Plan/plan_"+str(Numero_Reseau)+".txt &&"
    ligne4="docker kill test"
    command=ligne1+ligne2+ligne3+ligne4
    print(command)
    os.system(command)
    return 0

run_planner(6)