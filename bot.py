from fbchat import Client, log
from fbchat.models import *

class Paing(Client):
    def onMessage(
        self,
        mid=None,
        author_id=None,
        message=None,
        message_object=None,
        thread_id=None,
        thread_type=ThreadType.USER, **kwargs
    ):
        self.markAsRead(author_id)

        log.info("Message {} from {} in {}".format(message_object, thread_id, thread_type))
        msgText = message_object.text
        reply = 'Hello world'

        if author_id != self.uid:
            self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)

        self.markAsDelivered(author_id, thread_id)

class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        # If you're not the author, echo
        if author_id != self.uid:
            self.send(message_object, thread_id=thread_id, thread_type=thread_type)

client = EchoBot('thetpaimyo103@gmail.com', '581995TPM')
client.listen()
