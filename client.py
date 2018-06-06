import client_conf as c

name = input("Client name is: ")
client = c.client(name, "127.0.0.1", 9119)
client.create_connection()
client.mailing()
client.close_connection()
