from pyrogram import Client, filters
from pyrogram.types import InputMediaVideo, InputMediaDocument
from pymongo import MongoClient
from info import DATABASE_URI, DATABASE_NAME, COLLECTION_NAME, ADMINS, BOT_TOKEN

# Set up the MongoDB client
mongo_client = MongoClient(DATABASE_URI)
mongo_collection = mongo_client[DATABASE_NAME][COLLECTION_NAME]

# Define the admin user ID
ADMIN_USER_ID = ADMINS

# Create a Pyrogram client instance
app = Client("my_bot", bot_token=6216947279:AAEYIUjQMaL5XMB7MDz2C7kZM5PnZm0Hfc4, api_id=24081768, api_hash="15ead37b9f2c7cf765059a6406903261")

# Define a command handler for the /forward_all command
@app.on_message(filters.command("forward_all") & filters.user(ADMIN_USER_ID))
async def forward_all_command(client, message):
    # Get all files from the MongoDB collection
    files = mongo_collection.find()

    # Check if there are any files
    if files.count() == 0:
        await message.reply_text("There are no files in the database.")
        return

    # Get the channel name to forward the files to
    channel_name = message.text.split(" ", 1)[1]

    # Get the caption for the forwarded files
    caption = message.text.split(" ", 2)[2] if len(message.text.split()) > 2 else None

    # Counter for the number of files forwarded
    count = 0

    # Loop through all the files
    for file in files:
        # Get the file ID and file name
        file_id = file["file_id"]
        file_name = file["file_name"]

        # Forward the file to the specified channel
        if file_name.endswith((".mp4", ".mkv", ".avi", ".wmv", ".mov")):
            await client.send_video(channel_name, file_id, caption=caption)
        else:
            await client.send_document(channel_name, file_id, caption=caption)

        count += 1

    # Send a message with the number of files forwarded
    await message.reply_text(f"{count} files have been forwarded to {channel_name}.")

# Start the Pyrogram client
app.run()

