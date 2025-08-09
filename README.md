# Simple Discord Bot

This repository contains a minimal Discord bot demonstrating five basic commands and a message relay listener implemented using cogs.

## Commands
The following commands reside in `cogs/FunCog.py`:
- `!ping` – Responds with "Pong!" to check if the bot is running.
- `!greet` – Greets the user who invoked the command.
- `!roll [sides]` – Rolls a die with the given number of sides (defaults to six).
- `!flip` – Flips a coin and returns heads or tails.
- `!echo <message>` – Echoes back the provided message.

## Message Relay
`cogs/RelayCog.py` listens for all incoming messages and forwards them to the channel with ID `964663566366027826` in the guild with ID `842956728085118997`.

## Running the bot
1. Install dependencies: `pip install discord.py`
2. Set your Discord bot token in the `DISCORD_TOKEN` environment variable.
3. Start the bot with `python bot.py`.

This example is intentionally simple and meant for educational purposes.
