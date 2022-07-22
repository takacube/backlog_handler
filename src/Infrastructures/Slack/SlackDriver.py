import requests
class SlackDriver:
    def __init__(self, user, task, owner):
        self.user = user
        self.task = task
        self.owner = owner

    def notify(self):
        message = self.__create_msg(self.user, self.task, self.owner)
        requests.post(body="")






#private method
    def __create_msg(self, user, task, task_owner):
        return f"{task_owner}さんが{user}さんへ以下のタスクを登録しました。以下のURLから確認してください!\n{task}"
