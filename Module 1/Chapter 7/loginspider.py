class LoginSpider(BaseSpider):
    name = 'example.com'
    start_URLss = ['http://www.example.com/users/login.php']
    def parse(self, response):
        return [FormRequest.from_response(response, formdata={'username': 'john', 'password': 'secret'}, callback=self.after_login)]
    defafter_login(self, response):
        # check login succeed before going on
        if "authentication failed" in response.body:
            self.log("Login failed", level=log.ERROR)
            return
