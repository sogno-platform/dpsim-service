
import redis

# The hostname "redis" is set for development as an alias
# in the docker-compose.yaml file. For production this will
# resolve via the kubernetes service name
try:
    redis_connection = redis.Redis("redis")
except redis.exceptions.ConnectionError:
    redis_connection = None
    print("WARNING: Unable to connect to redis. No problem on test.")

# TEST ONLY
def overwrite_connection(connection):
    global redis_connection
    redis_connection = connection

def get_logs(analysis_id):
    return get_files(analysis_id, "logs")

def add_log(analysis_id, filename, data):
    return add_file(analysis_id, "logs", filename, data)

def get_results(analysis_id):
    return get_files(analysis_id, "results")

def add_result(analysis_id, filename, data):
    return add_file(analysis_id, "results", filename, data)

def get_files(analysis_id, filetype):
    """Get a set of result files

    :param id: analysis id
    :type id: int

    :rtype: dict of text strings
    """
    filelist = redis_connection.smembers(str(analysis_id) + "_" + filetype)
    files = {}
    for filename_bytes in filelist:
        filename = filename_bytes.decode("utf-8")
        files[filename] = redis_connection.get(filename).decode("utf-8")
    return files

def add_file(analysis_id, filetype, filename, data):
    """Store logs in the db

    :param analysis_id: the id of the analysis
    :param files: the log files
    :rtype: integer
    """
    redis_connection.sadd(str(analysis_id) + "_" + filetype, str(filename))
    redis_connection.set(str(filename), data)
    return

