from mycroft import MycroftSkill, intent_file_handler


class NotFeelingGood(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('good.feeling.not.intent')
    def handle_good_feeling_not(self, message):
         = message.data.get('')

        self.speak_dialog('good.feeling.not', data={
            '': 
        })


def create_skill():
    return NotFeelingGood()

