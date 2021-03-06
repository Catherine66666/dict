import psycopg2
conn = psycopg2.connect(
   host="localhost",
   database="database",
   user="user1",
   password="abc123"
)

print('Hello and welcome to the phone list, available commands:')
print('  add    - add a word')
print('  delete - delete a word')
print('  list   - list all words')
print('  quit   - quit the program')

# read_dict: returns the list of all dictionary entries:
#   argument: Conn - the database connection.
def read_dict(conn):
    cur = conn.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    return rows
# add_word: adds entries into dictionary:
#   argument: Conn - the database connection
#             word - english word
#             translation - swedish translation.
def add_word(conn, word, translation):
    cur = conn.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()
# delete_word: deletes entries from dictionary:
#   argument: Conn - the database connection
#             ID - ID of the entry.
def delete_word(conn, ID):
    cur = conn.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()
# save_dict: saves dictionary:
#   argument: Conn - the database connection
def save_dict(conn):
    cur = conn.cursor()
    cur.execute("COMMIT;")
    cur.close()
def main():
    while True: ## REPL - Read Execute Program Loop
    cmd = input("Command: ")
    if cmd == "list":
        for i, wd, trans in read_dict(conn):
            print(f"{i}: {wd} - {trans}")
    elif cmd == "add":
        name = input("  Word: ")
        phone = input("  Translation: ")
        add_word(conn, name, phone)
        print(f"Added word {name}")
    elif cmd == "delete":
        ID = input("  ID: ")
        cur = conn.cursor()
        name = cur.execute(f"SELECT word FROM dictionary where id = '{ID}';")
        print(f"Word {name} is removed. I need some help fixing this printout")
        delete_word(conn, ID)
    elif cmd == "quit":
        save_dict(conn)
        print("Dictionary is saved and closed")
        exit()

main()
