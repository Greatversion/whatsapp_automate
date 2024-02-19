# WhatsApp Automation

This project is a simple automation script written in Python using Selenium to send messages on WhatsApp Web.

## Description

The script automates the process of sending a specified message to a WhatsApp contact multiple times. It utilizes Selenium, a powerful tool for automating web browsers, to interact with the WhatsApp Web interface.

## Prerequisites

Before running the script, ensure you have the following installed:
- Python 3.x
- Chrome browser
- ChromeDriver (ensure it's compatible with your Chrome browser version)

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/your-username/whatsapp-automation.git
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Download and install ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads). Make sure to place the `chromedriver.exe` file in your system's PATH or in the same directory as the script.

## Usage

1. Run the script:
    ```bash
    python whatsapp_automation.py
    ```

2. Scan the QR code with your phone to log in to WhatsApp Web.

3. Wait for the script to find the specified contact and start sending messages.

4. You can modify the script to send different messages or to send messages to different contacts by changing the variables in the script.

## Configuration

You can customize the script by modifying the following variables in the script:
- `target`: Specify the name of the contact you want to send messages to.
- `message`: Specify the message you want to send.
- `number_of_times`: Specify the number of times you want to send the message.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

