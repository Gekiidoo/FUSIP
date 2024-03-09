
🛡️ **FUSIP** is a **Python**-based tool designed for professionals to train and test IP vulnerabilities, featuring IP scanning and DDOS attack functionalities. FUSIP empowers users to analyze IP addresses, generate images with embedded scripts, and execute DDOS attacks for educational and testing purposes.

## Features 👀

**1. IP Scan (IPv4 only)** 🤖
   - Conduct detailed analysis of IPv4 addresses.
   - Retrieve information including country, city, latitude, longitude, and Internet Service Provider (ISP).
   - Utilizes the IPInfo.io API for accurate data retrieval.

**2. IP DDOS (Distributed Denial of Service)** ☠️
   - Perform simulated DDOS attacks on specified IP addresses.
   - Specify the number of connections to establish, creating a distributed attack scenario.
   - Utilizes multi-threading to efficiently establish connections.

**3. IP Grabber** 🎯
   - Generate images with embedded scripts to obscure malicious content.
   - Utilizes Piexif library to embed script content in image metadata.
   - Users can rename the generated image for further deployment.

## Usage

1. Clone the repository to your local machine.
2. Ensure you have Python installed along with required dependencies (PyFiglet, Piexif, Pillow).
3. Obtain an API key from [IPInfo.io](https://ipinfo.io) and replace `API_KEY` variable with your key in the code.
4. Run the `fusip.py` script.
5. Follow on-screen prompts to choose between IP scanning, DDOS attack, or IP grabbing functionalities.
6. Input the required information and analyze results.

### Disclaimer

⚠️ FUSIP is intended for educational and testing purposes only. Misuse of this tool for malicious activities is strictly prohibited. The developers do not endorse any illegal or unethical use of this tool and are not responsible for any damages resulting from such activities.

### Contributions

🤝 Contributions to FUSIP are welcome! If you have any suggestions, improvements, or feature requests, feel free to open an issue or submit a pull request on GitHub.
Made by Gekidoo :D

### License

📜 FUSIP is distributed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to modify and distribute the code as per the terms of the license.

## Installation

To install the required dependencies for running FUSIP, follow these steps:

**1. Clone the GitHub repository:**
   ```bash
   git clone https://github.com/Gekiidoo/FUSIP.git
   ```

**2. Navigate to the FUSIP directory:**
   ```bash
   cd FUSIP
   ```

**3. Install dependencies via pip:**
   ```bash
   pip install -r requirements.txt
   ```
**if you have any error with the requirements.txt , you can do this instead**
```bash
   pip install Pillow
   pip install pyfiglet
   pip install requests
   pip install piexif
```

   Make sure to run this command in a Python virtual environment if necessary.

**4. Configure the IPInfo.io API key:**
   - Get a free API key from [IPInfo.io](https://ipinfo.io).
   - Replace the value of the `API_KEY` variable in the `fusip.py` file with your API key.

**5. Run FUSIP**
   ```bash
   python FUSIP.py
   ```

**if you want any help , join my discord : https://discord.gg/SrJgUTQcAH**
Enjoy 😘


