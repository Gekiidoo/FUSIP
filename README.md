
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


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🛡️ **FUSIP** est un outil basé sur **Python** conçu pour permettre aux professionnels de former et de tester les vulnérabilités IP, offrant des fonctionnalités de balayage IP et d'attaque DDOS. FUSIP permet aux utilisateurs d'analyser les adresses IP, de générer des images avec des scripts intégrés et d'exécuter des attaques DDOS à des fins éducatives et de test.

## Fonctionnalités 👀

**1. Balayage IP (IPv4 uniquement)** 🤖
   - Effectuez une analyse détaillée des adresses IPv4.
   - Récupérez des informations telles que le pays, la ville, la latitude, la longitude et le fournisseur de services Internet (ISP).
   - Utilise l'API IPInfo.io pour une récupération précise des données.

**2. IP DDOS (Déni de service distribué)** ☠️
   - Effectuez des attaques DDOS simulées sur des adresses IP spécifiées.
   - Spécifiez le nombre de connexions à établir, créant ainsi un scénario d'attaque distribuée.
   - Utilise le multithreading pour établir efficacement des connexions.

**3. IP Grabber** 🎯
   - Générez des images avec des scripts intégrés pour dissimuler du contenu malveillant.
   - Utilise la bibliothèque Piexif pour intégrer le contenu du script dans les métadonnées de l'image.
   - Les utilisateurs peuvent renommer l'image générée pour un déploiement ultérieur.

## Utilisation

1. Clonez le dépôt sur votre machine locale.
2. Assurez-vous d'avoir Python installé ainsi que les dépendances requises (PyFiglet, Piexif, Pillow).
3. Obtenez une clé API auprès de [IPInfo.io](https://ipinfo.io) et remplacez la variable `API_KEY` par votre clé dans le code.
4. Exécutez le script `fusip.py`.
5. Suivez les instructions à l'écran pour choisir entre les fonctionnalités de balayage IP, d'attaque DDOS ou de capture IP.
6. Entrez les informations requises et analysez les résultats.

### Avis de non-responsabilité

⚠️ FUSIP est destiné uniquement à des fins éducatives et de test. L'utilisation abusive de cet outil à des fins malveillantes est strictement interdite. Les développeurs ne cautionnent aucune utilisation illégale ou non éthique de cet outil et ne sont pas responsables des dommages résultant de telles activités.

### Contributions

🤝 Les contributions à FUSIP sont les bienvenues ! Si vous avez des suggestions, des améliorations ou des demandes de fonctionnalités, n'hésitez pas à ouvrir une issue ou à soumettre une pull request sur GitHub.
Créé par Gekidoo :D

### Licence

📜 FUSIP est distribué sous la [Licence MIT](https://opensource.org/licenses/MIT). N'hésitez pas à modifier et distribuer le code selon les termes de la licence.

## Installation

Pour installer les dépendances requises pour exécuter FUSIP, suivez ces étapes :

**1. Clonez le dépôt GitHub :**
   ```bash
   git clone https://github.com/Gekiidoo/FUSIP.git
   ```

**2. Accédez au répertoire FUSIP :**
   ```bash
   cd FUSIP
   ```

**3. Installez les dépendances via pip :**
   ```bash
   pip install -r requirements.txt
   ```
**si vous rencontrez une erreur avec le fichier requirements.txt, vous pouvez faire cela à la place**
```bash
   pip install Pillow
   pip install pyfiglet
   pip install requests
   pip install piexif
```
   Assurez-vous d'exécuter cette commande dans un environnement virtuel Python si nécessaire.

**4. Configurez la clé API IPInfo.io :**
   - Obtenez une clé API gratuite sur [IPInfo.io](https://ipinfo.io).
   - Remplacez la valeur de la variable `API_KEY` dans le fichier `fusip.py` par votre clé API.

**5. Exécutez FUSIP**
   ```bash
   python FUSIP.py
   ```

**si vous avez besoin d'aide, rejoignez mon discord : https://discord.gg/SrJgUTQcAH**
Amusez-vous bien 😘

