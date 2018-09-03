import queue
from io import BytesIO


incoming_msg_queue = queue.Queue()


class CommonMsg():
    is_skype = False
    is_telegram = False
    chat_id = None
    user = {'id': None, 'name': None}
    time = None
    content = None
    content_full = None
    file_obj = {'name': None, 'obj': None}


def bytes_to_object(content, name):
    file_obj = BytesIO(content)
    file_obj.name = name
    return file_obj
