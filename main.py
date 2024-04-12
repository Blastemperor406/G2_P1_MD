import os
import sys
import subprocess
from colorama import Fore, Style

def create_cron_job(schedule, command):
    cron_command = f'(crontab -l ; echo "{schedule} {command}") | crontab -'
    subprocess.call(cron_command, shell=True)
    print(f"{Fore.GREEN}Cron job created successfully!{Style.RESET_ALL}")

def main():
    print(f"{Fore.CYAN}Welcome to S.I.F.S!{Style.RESET_ALL}")
    schedule = input("Enter schedule (in crontab format, e.g., '0 0 * * *' for daily): ")
    docker_compose_file = "producer-docker-compose.yaml"
    

    # Check if Docker Compose file exists
    if not os.path.exists(docker_compose_file):
        print(f"{Fore.RED}Error: Docker Compose file not found!{Style.RESET_ALL}")
        sys.exit(1)

    command = f"docker-compose -f {docker_compose_file} up -d"
    create_cron_job(schedule, command)

if __name__ == "__main__":
    main()
