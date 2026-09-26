from locust import HttpUser, task, between


class JSONPlaceholderUser(HttpUser):
    wait_time = between(1, 3)
    host = "https://jsonplaceholder.typicode.com"

    @task(3)
    def get_posts(self):
        self.client.get("/posts")

    @task(2)
    def get_single_post(self):
        self.client.get("/posts/1")

    @task(1)
    def get_nonexistent_post(self):
        self.client.get("/posts/99999")
