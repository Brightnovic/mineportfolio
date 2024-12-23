from django.apps import AppConfig
import threading
import requests
import time

# Infinite loop to keep the server active
def keep_alive():
    URL = "https://mineportfolio-wvfa.onrender.com/"  # Replace with your endpoint
    while True:
        try:
            response = requests.get(URL)
            if response.status_code == 200:
                print("Server is active!")
            else:
                print(f"Unexpected response: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(300)  # 5 minutes delay


# Start the keep-alive process
def start_keep_alive():
    thread = threading.Thread(target=keep_alive)
    thread.daemon = True  # Ensures thread stops when the server stops
    thread.start()


# AppConfig for Django app
class PortfolioConfig(AppConfig):  # Replace 'PortfolioConfig' with your app's name
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio'  # Replace 'portfolio' with your app name

    def ready(self):
        # Start the keep-alive process only once
        print("Starting keep-alive process...")
        start_keep_alive()
