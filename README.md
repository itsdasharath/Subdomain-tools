# subD.py

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Description
subD.py is a Python script that performs subdomain enumeration for a given domain. It utilizes threading to efficiently discover subdomains by sending HTTP requests to potential subdomains and checking their availability. The script provides a fast and comprehensive list of active subdomains associated with the target domain.

## Features
- Subdomain enumeration using threading for concurrency.
- Fast and efficient discovery of active subdomains.
- User-friendly output format.
- Easy integration with custom subdomain wordlists.

## Installation
1. Clone the repository:
    ```shell
    git clone https://github.com/your-username/subD.py.git
    ```
2. Navigate to the project directory:
    ```shell
    cd subD.py
    ```
3. Install the required dependencies:
    ```shell
    pip install -r requirements.txt
    ```

## Usage
1. Prepare your subdomain wordlist (if not using the default one):
    - Add your wordlist to the `wordlists/` directory or specify its path when prompted.

2. Run the script:
    ```shell
    python subD.py
    ```
    - You will be prompted to enter the target domain. The script will then enumerate subdomains and output the discovered ones.


## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

