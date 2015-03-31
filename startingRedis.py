# kunalprompt.github.io
# Gearing up with (Re)mote(di)ctionary(s)erver
# Install - sudo pip install redis
# $ redis-server
# check server state whether running or not - $ redis-cli ping
# and the reponse has to be PONG for running state


# importing redis library
import redis

# initiating redis instance - there are two ways both mean the same - one for backward compatibility and another for forward
# r = redis.Redis(host='localhost', port=6379, db=0, password=None, socket_timeout=None, connection_pool=None, charset='utf-8', errors='strict', unix_socket_path=None)
# r = redis.StrictRedis(host='localhost', port=6379, db=0, password=None, socket_timeout=None, connection_pool=None, charset='utf-8', errors='strict', unix_socket_path=None)

r = redis.Redis()

# setting a key
r.set('firstName', 'Kunal')
r.set('lastName', 'Sharma')

# get the keys
print r.get('firstName')
print r.get('lastName')