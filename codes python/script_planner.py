import os
import subprocess
import time
path=os.path.dirname(os.path.dirname(__file__))
#fonction pour savoir si docker tourne
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
#fonction pour lancer docker desktop    
def start_docker_desktop():
    # Path to Docker Desktop executable on Windows
    docker_path = r"C:\Program Files\Docker\Docker\Docker Desktop.exe"
    
    try:
        # Start Docker Desktop
        os.startfile(docker_path)
        print("Starting Docker Desktop...")

    except Exception as e:
        print(f"Failed to start Docker Desktop: {e}")
#permet de savoir si le container portant le même nom existe deja pour ensuite le supprimer si c'est le cas
def check_container_exists(container_name):
    try:
        # Exécute la commande Docker pour lister les conteneurs (actifs et inactifs)
        result = subprocess.run(['docker', 'ps', '-a', '--filter', f'name={container_name}', '--format', '{{.Names}}'],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Vérifie si la sortie contient le nom du conteneur
        if container_name in result.stdout.splitlines():
            return True
        else:
            return False
    except Exception as e:
        print(f"Une erreur s'est produite: {e}")
        return False




#fonction qui vérifier que docker est lancé et le run si ce n'est pas le cas 
#run l'image LAPKT avec le dossier Automated-AI-Distribution-Network comme mount dans un container nommé test
#run le planner avec le problem au numéro du réseau indiqué 
#déplace le plan dans le dossier plan 
#puis supprime le container test

def run_planner(Numero_Reseau,methode="dfs_plus",domain="domainv8.pddl"):
    if is_docker_running() ==False:
        start_docker_desktop()
        timeout = 120  # Timeout in seconds (1 minutes)
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            time.sleep(5)
    if is_docker_running() ==True:
        if check_container_exists("test")==True:
            subprocess.run(['docker', 'rm', '-f', "test"], check=True)
        ligne1 = ["docker", "run", "--name", "test", "-it", "-d", "--rm", "-v", f"{path}:/root/projects/benchmarks", "lapkt/lapkt-public"]
        ligne2 = ["docker", "exec", "-it", "test", f"./{methode}", 
            "--domain", f"/root/projects/benchmarks/CSV_Problem/{domain}",
            "--problem", f"/root/projects/benchmarks/CSV_Problem/problem_{Numero_Reseau}.pddl"]

        ligne3 = ["docker", "exec", "-it", "test", "cp", 
            "/root/projects/lapkt/compiled_planners/plan.ipc", f"/root/projects/benchmarks/Plan/plan_{Numero_Reseau}.txt"]
        ligne4 = ["docker", "kill", "test"]
        subprocess.run(ligne1, check=True)
        subprocess.run(ligne2, check=True)
        subprocess.run(ligne3, check=True)
        subprocess.run(ligne4, check=True)
    return 0
