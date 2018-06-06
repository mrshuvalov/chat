import server_conf as s
server = s.server('127.0.0.1', 9119)
server.create_connection()
server.messaging()