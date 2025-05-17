from zk import ZK, const

conn = None
# create ZK instance
zk = ZK('192.168.1.201', port=4370, timeout=5)

def test_zk_connection(conn):
    try:
        print("Connecting to ZK device...")
        conn = zk.connect()
        users = conn.get_users()
        for user in users:
            privilege = 'User'
            if user.privilege == const.USER_ADMIN:
                privilege = 'Admin'

            print('- UID #{}'.format(user.uid))
            print('  Name       : {}'.format(user.name))
            print('  Privilege  : {}'.format(privilege))
            print('  User  ID   : {}'.format(user.user_id))

        print("Voice Test ...")
        conn.test_voice()
        
    except Exception as e:
        print("Error connecting to ZK device: " + str(e))
    finally:
        if conn:
            conn.disconnect()
            print("Disconnected from ZK device.")

if __name__ == "__main__":
    test_zk_connection(conn)