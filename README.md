# Discord Bot Notifier

The Discord Bot Notifier script enables you to receive critical messages from a designated Discord channel on your phone via SMS using Twilio. This README will guide you through the setup and usage.

## Getting Started

### Prerequisites

Before getting started, make sure you have the following:

- A Discord account and access to a Discord server where you want to monitor a specific channel.
- A Twilio account for sending SMS notifications.

### Setup Instructions

1. **Create a Discord Bot:**

   - Visit the [Discord Developer Portal](https://discord.com/developers/applications).
   - Create a new application and add a bot to it.
   - Copy the bot token provided by Discord.

2. **Configure Twilio:**

   - Sign up for an account on [Twilio](https://www.twilio.com/).
   - Obtain your Twilio account SID and authentication token from the Twilio dashboard.

3. **Clone the Repository:**

   - Clone this repository to your local machine or server where you intend to run the script.

4. **Install Dependencies:**

   - Open your terminal and navigate to the project directory.
   - Run the following command to install the required dependencies:

     ```bash
     pip install discord pytwilio
     ```

5. **Modify the Script:**

   - Open the `bot_notifier.py` script in a code editor.
   - Replace the following placeholders with your actual credentials:
   
     - `YOUR_DISCORD_BOT_TOKEN`: Replace with your Discord bot token obtained in step 1.
     - `YOUR_TWILIO_ACCOUNT_SID`: Replace with your Twilio account SID.
     - `YOUR_TWILIO_AUTH_TOKEN`: Replace with your Twilio authentication token.
     - `YOUR_PHONE_NUMBER`: Replace with your phone number in E.164 format (e.g., `+1234567890`).
     - `TWILIO_PHONE_NUMBER`: Replace with your Twilio phone number.

6. **Configure the Discord Channel and Phone Number:**

   - Modify the `message.channel.id` to match the ID of the Discord channel you want to monitor.
   - Ensure that you've provided both your phone number and the Twilio phone number accurately.

7. **Run the Script:**

   - Execute the script using the following command:

     ```bash
     python bot_notifier.py
     ```

## Usage

Once the script is running, it will continuously monitor the specified Discord channel. When a new message is posted in that channel, you will receive an SMS notification on your configured phone number via Twilio.

## Important Notes

- Ensure that the Discord bot has the necessary permissions in your Discord server, including reading messages from the designated channel.
- Use this script responsibly and respect the privacy and terms of service of both Discord and Twilio.

Feel free to customize and extend the script to suit your specific needs. Enjoy staying connected with your Discord community, even while on the go!
