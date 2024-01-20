# Web Scraper Project

This project contains a Python script that uses Selenium to scrape job listings from a website.

## Description

The `scraper.py` script navigates to a specific URL, iterates through job listings, and logs details about each job. It operates in headless mode, which means it does not require a graphical user interface to run.

## Prerequisites

Before running this script, you must have the following installed:

- Python 3.6 or higher
- pip (Python package installer)
- Selenium WebDriver
- ChromeDriver (make sure it's in your PATH)

This script was tested on macOS, but it should work on other operating systems that support Python and Selenium.

## Installation

To set up the project, follow these steps:

1. **Clone the repository**: Clone the repository to your local machine using the command below:
   git clone https://github.com/Nikitaamo/scraper-nk-1.git
   cd scraper-nk-1

3. **Set up a Python virtual environment**: Create a virtual environment in the project directory:
python3 -m venv venv

4. **Activate the virtual environment**: Activate the virtual environment to use it:
On macOS and Linux:
source venv/bin/activate
On Windows:
.\venv\Scripts\activate

5. **Install the required packages**: Install the required Python packages using pip:
pip3 install -r requirements.txt

6. ** upgrade selenium pip3 install --upgrade selenium

7. ## Usage
To run the script, make sure your virtual environment is activated, and execute the following command:
python3 scraper.py

The script will start scraping the website in headless mode. All logs will be saved to `main.log`.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Contribution

Contributions to this project are welcome. Please fork the repository and submit a pull request.

## Contact

For questions or feedback regarding the script, please file an issue in this repository.
