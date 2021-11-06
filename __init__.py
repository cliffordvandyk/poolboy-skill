from mycroft import MycroftSkill, intent_file_handler


class Poolboy(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('poolboy.intent')
    def handle_poolboy(self, message):
        self.speak_dialog('poolboy')


def create_skill():
    return Poolboy()

