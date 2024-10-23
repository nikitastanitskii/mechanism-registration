import bcrypt
import redis


redis_connector = redis.Redis(host='localhost', port=6379, db=0)