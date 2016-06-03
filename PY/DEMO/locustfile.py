# coding=utf-8
from locust import HttpLocust, TaskSet, task
import json


class UserBehavior(TaskSet):

    token = ''
    userId = ''
    headers = ''

    def login(self):
        data = {
            "email": "demo@uyunsoft.cn",
            "passwd": "fe01ce2a7fbac8fafaed7c982a04e229",
        }
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'}
        response = self.client.post(
            'tenant/api/v1/user/login',
            data=json.dumps(data),
            headers=headers)
        content = json.loads(response.content)
        self.token = {"token": content['data']['token']}
        self.userId = content['data']['userId']

    def logout(self):
        with self.client.get('tenant/api/v1/user/logout', params=self.token, catch_response=True) as response:
            if response.status_code != 200:
                response.failure()

    def user_details(self):
        data = {'userId': self.userId}
        with self.client.get('tenant/api/v1/user/details/view', params=data, headers=self.headers, catch_response=True) as response:
            if response.status_code != 200:
                response.failure()

    @task(10)
    def login_logout(self):
        self.login()
        self.user_details()
        self.logout()

class WebsiteUser(HttpLocust):
    host = 'http://10.1.51.221:7600/'
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000