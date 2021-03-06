import queue
from common import CommonMsg, bytes_to_object


def escape_tags(text):
    text = text.replace('<<<', '&lt;&lt;&lt;')
    return text

def parse_incoming_msg(sk_msg):

    def content_full(msg):
        return  f"[{msg.user['name']}] {msg.content}"

    msg = CommonMsg()
    msg.is_skype = True
    if hasattr(sk_msg, 'markup'):
        msg.content = escape_tags(sk_msg.markup)
    msg.chat_id = sk_msg.chatId
    msg.user = {
            'id': sk_msg.user.id,
            'name': str(sk_msg.user.name)}
    msg.time = sk_msg.time

    if hasattr(sk_msg, 'file'):
        if sk_msg.file.urlThumb:
            file_obj = bytes_to_object(sk_msg.fileContent, sk_msg.file.name)
            msg.file_obj = {
                    'name': sk_msg.file.name,
                    'obj': file_obj}
            msg.content = sk_msg.file.name

    msg.content_full = content_full(msg)
    return msg

def parse_incoming_event(sk_event):
    msg = CommonMsg()
    msg.is_skype = True
    msg.chat_id = sk_event.chat.id
    if sk_event.type == 'ThreadUpdate':
        msg.is_cmd = True
        msg.cmd_conversation_name = sk_event.chat.topic
    return msg
