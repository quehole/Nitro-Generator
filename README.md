# Nitro Generator

Nitro Generator is a Discord bot that offers various functionalities including kicking, banning members, clearing messages, generating and sending Nitro codes, and more. This bot uses the Discord API to interact with server members and channels.

## Features

- **Kick Members**: Kick a member from the server.
- **Ban Members**: Ban a member from the server.
- **Clear Messages**: Clear all messages in the current channel.
- **Generate Nitro Codes**: Generate and send Nitro codes based on user roles.
- **Drop Nitro Codes**: Send a large number of Nitro codes to the channel.
- **Create Tickets**: Create a private ticket channel for support or queries.
- **DM Users**: Send direct messages to users.
- **Help Command**: Provides a list of available commands.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/quehole/Nitro-Generator.git
   cd Nitro-Generator
   ```

2. **Install Dependencies**

   Ensure you have Python installed, then install the required packages:

   ```bash
   pip install discord.py
   ```

3. **Configure the Bot**

   - Open `main.py`.
   - Replace the placeholder values:
     - `token` with your Discord bot token.
     - `admins` with your Discord user ID.
     - `welcome` with the ID of the welcome channel.
     - `bots_channel` with the ID of the bot command channel.
     - `whitelist` with a list of whitelisted user IDs.

4. **Run the Bot**

   ```bash
   python main.py
   ```

## Usage

1. **Commands**:

   - `$kick [user] [reason]`: Kick a member from the server.
   - `$ban [user] [reason]`: Ban a member from the server.
   - `$clear`: Clear all messages in the current channel.
   - `$nitro`: Generate and send Nitro codes based on the user's role.
   - `$drop`: Send a large number of Nitro codes to the channel.
   - `$ticket`: Create a private ticket channel for support.
   - `$dm [user_id] [message]`: Send a direct message to a specified user.
   - `$help`: Show the list of available commands.

2. **Permissions**:

   Ensure the bot has the appropriate permissions in your server, including message management and member management permissions.

## Notes

- Modify the `nitro_timeout` and other configuration variables as needed.
- Ensure you handle bot tokens securely and do not share them publicly.
- Review and comply with Discord's [Terms of Service](https://discord.com/terms) and [Developer Terms](https://discord.com/developers/docs/legal).

## Author

Created by [quehole](https://github.com/quehole). For further assistance or questions, please refer to the GitHub repository.
