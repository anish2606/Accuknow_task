import os
import subprocess
import logging
from datetime import datetime

# Configure logging for backup
logging.basicConfig(filename='backup.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

BACKUP_SOURCE = '/home/user/documents'  # Example: Change to your actual source directory  # Change this to your source directory
BACKUP_DESTINATION = 'user@192.168.1.100:/backup/'  # Example: Change to your actual remote backup location  # Change this to your remote server

def backup_directory():
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_log = f'backup_{timestamp}.log'
    
    command = ["rsync", "-avz", BACKUP_SOURCE, BACKUP_DESTINATION]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        with open(backup_log, 'w') as log_file:
            log_file.write(result.stdout)
        logging.info("Backup completed successfully.")
        print("Backup completed successfully.")
    except subprocess.CalledProcessError as e:
        with open(backup_log, 'w') as log_file:
            log_file.write(e.stderr)
        logging.error("Backup failed!")
        print("Backup failed!")

if __name__ == "__main__":
    backup_directory()

