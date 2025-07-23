# 📚 Kindle Highlights Telegram Bot

A simple Telegram bot that allows you to import highlighted text from Kindle to Telegram and receive random highlights as messages. You can schedule the bot to send you a random highlight at regular intervals, or manually request a highlight.

## ✨ Features

- **Import Highlights**: Upload a `.txt` file containing your Kindle highlights, and the bot will process and store them.
- **Receive Highlights**: Use commands to request random highlights from your imported collection.
- **Scheduled Highlights**: Set up a schedule to receive random highlights at regular intervals (e.g., every 1 minute, 5 minutes, etc.).
- **Manage Schedules**: Easily set or delete highlight schedules through bot commands.
- **Database Storage**: Uses PostgreSQL for reliable data persistence.

## 📋 Prerequisites

- Python 3.8+
- A Telegram account and a Telegram Bot API token (see instructions below)
- PostgreSQL database (automatically handled on Render)

## 🚀 Getting Started

### 1. Create a Bot

1. Go to [BotFather](https://t.me/BotFather) on Telegram.
2. Use `/newbot` to create a new bot and get the API token.
3. Copy the token, as you will need it later.

### 2. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/hungnguyen7/kindle-highlight-telegram-bot.git
cd kindle-highlight-telegram-bot
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Configure the Bot

1. Create a new file named `.env` in the project root directory.
2. Add the following lines to the `.env` file:

```plaintext
BOT_TOKEN=your_bot_token_here
DATABASE_URL=postgresql://username:password@localhost:5432/dbname
```

Replace `your_bot_token_here` with the API token you received from BotFather.
The `DATABASE_URL` is required and should point to your PostgreSQL database.

### 5. Run the Bot

Start the bot by running the following command:

```bash
python bot.py
```

The bot should now be running and ready to receive commands.

## 🌐 Deploy to Render

This bot is ready to deploy on [Render](https://render.com) with PostgreSQL:

1. Fork this repository to your GitHub account
2. Connect your GitHub account to Render
3. Create a new service and select this repository
4. Render will automatically detect the `render.yaml` file and set up:
   - A PostgreSQL database
   - A worker service for the bot
5. Add your `BOT_TOKEN` environment variable in the Render dashboard
6. Deploy!

### 📜 Commands

The bot supports the following commands:

- `/start`: Start the bot and view the available commands.
- `/help`: View the available commands.
- `/import`: Import a `.txt` file containing Kindle highlights.
- `/highlight`: Get a random highlight from your collection.
- `/schedule`: Set up a schedule to receive random highlights at regular intervals.
- `/unschedule`: Stop receiving scheduled highlights.

