import os
import subprocess
import time
path=os.path.dirname(os.path.dirname(__file__))
def is_docker_running():
    try:
        # Execute a simple Docker command
        result = subprocess.run(['docker', 'info'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Check the return code. If it's 0, Docker is running.
        if result.returncode == 0:
            return True
        else:
            return False

    except FileNotFoundError:
        # Docker command not found (Docker is likely not installed)
        return False
    
def start_docker_desktop():
    # Path to Docker Desktop executable on Windows
    docker_path = r"C:\Program Files\Docker\Docker\Docker Desktop.exe"
    
    try:
        # Start Docker Desktop
        os.startfile(docker_path)
        print("Starting Docker Desktop...")

    except Exception as e:
        print(f"Failed to start Docker Desktop: {e}")
def run_planner(Numero_Reseau,methode="dfs_plus",domain="domainv8.pddl"):
    if is_docker_running() ==False:
        start_docker_desktop()
        timeout = 60  # Timeout in seconds (1 minutes)
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            time.sleep(5)
    if is_docker_running() ==True:
        ligne1="docker run --name test -it -d --rm -v "+path+":/root/projects/benchmarks lapkt/lapkt-public &&"
        ligne2="docker exec -it test ./"+methode+" --domain /root/projects/benchmarks/CSV_Problem/"+domain+" --problem /root/projects/benchmarks/CSV_Problem/problem_"+str(Numero_Reseau)+".pddl &&"
        ligne3="docker exec -it test cp /root/projects/lapkt/compiled_planners/plan.ipc /root/projects/benchmarks/Plan/plan_"+str(Numero_Reseau)+".txt &&"
        ligne4="docker kill test"
        command=ligne1+ligne2+ligne3+ligne4
        os.system(command)
    return 0

run_planner(6)
