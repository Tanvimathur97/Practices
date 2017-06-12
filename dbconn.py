import MySQLdb


host = input('Host: ')
user = input('Username: ')
passwd = input('Password: ')

conn = MySQLdb.connect(host=host, user=user, passwd=passwd)
cursor = conn.cursor()

ans = int(input('What do you want to do?'
            '1. Create Database'
            '2. Show Database'
            '3. Exit'
            'Enter here: '))
# I changed here
while ans != 0:
    if ans == 1:
        db = input('Enter the name of database you want to create: ')
        cursor.execute('''CREATE DATABASE IF NOT EXISTS ''' + db + ';'
                                                                   'Enter here: ')

