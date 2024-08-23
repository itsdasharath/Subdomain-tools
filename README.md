# subD.py

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Description
subD.py is a Python script that performs subdomain enumeration for a given domain. It utilizes threading to efficiently discover subdomains by sending HTTP requests to potential subdomains and checking their availability. The script provides a fast and comprehensive list of active subdomains associated with the target domain.

## Features
- Fast subdomain enumeration using threading.
- Option to use custom wordlists or default wordlist.
- Handles errors related to missing or unreadable wordlists.
- User-friendly and flexible command-line interface.

## Installation
1. Clone the repository:
    ```shell
    git clone https://github.com/itsdasharath/Subdomain-tools.git
    ```
2. Navigate to the project directory:
    ```shell
    cd Subdomain-tools
    ```
3. Install the required dependencies:
    ```shell
    pip install -r requirements.txt
    ```

## Usage
1. Prepare your subdomain wordlist (if not using the default one):
    -specify its path when prompted.

2. Run the script:
    ```shell
    python subD.py -d example.com 
    ```
    - Replace example.com with your target domain and custom_wordlist.txt with your wordlist. If the custom wordlist is not available, you'll be prompted to use the default wordlist.

## Option
- `-d` or `--domain`: Specify the target domain.{required}
- `-w` or `--wordlist`: Specify the path to the custom wordlist. {optional: default wordlist will be used if not provided}


## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

