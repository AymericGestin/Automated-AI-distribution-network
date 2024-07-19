from code_ecriture import *
import os
os.system("docker run -it lapkt/lapkt-public")
os.system("./siw --domain ../benchmarks/ipc-2011/visitall/domain.pddl --problem ../benchmarks/ipc-2011/visitall/problem12.pddl")
#os.system('cmd /k "docker run -it "+path+":/root/projects/benchmarks lapkt/lapkt-public"')
#./siw_plus --domain /root/projects/benchmarks/CSV_Problem/domainv8.pddl --problem /root/projects/benchmarks/CSV_Problem/problem_16.pddl

#os.system('cmd /c "exit"') 