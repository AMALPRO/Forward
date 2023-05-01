DATABASE_URI = environ.get('DATABASE_URI', "amalser")
DATABASE_NAME = environ.get('DATABASE_NAME', "mongodb+srv://amal:amal@cluster0.dlmfo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1869495895').split()]
