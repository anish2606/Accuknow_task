import psutil
import logging
  
  # Configure logging for system health monitoring
logging.basicConfig(filename='system_health.log', level=logging.INFO, 
                      format='%(asctime)s - %(levelname)s - %(message)s')
  
  # System Health Monitoring
CPU_THRESHOLD = 80  # Percentage
MEMORY_THRESHOLD = 80  # Percentage
DISK_THRESHOLD = 80  # Percentage
  
def check_system_health():
      cpu_usage = psutil.cpu_percent(interval=1)
      memory_usage = psutil.virtual_memory().percent
      disk_usage = psutil.disk_usage('/').percent
      
      alerts = []
      
      if cpu_usage > CPU_THRESHOLD:
          alerts.append(f'High CPU usage detected: {cpu_usage}%')
      if memory_usage > MEMORY_THRESHOLD:
          alerts.append(f'High Memory usage detected: {memory_usage}%')
      if disk_usage > DISK_THRESHOLD:
          alerts.append(f'High Disk usage detected: {disk_usage}%')
      
      if alerts:
          for alert in alerts:
              logging.warning(alert)
              print(alert)
      else:
          logging.info("System health is normal.")
          print("System health is normal.")
  
if __name__ == "__main__":
      check_system_health()
