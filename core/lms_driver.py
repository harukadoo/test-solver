from playwright.sync_api import Page, expect
import time

class LmsDriver:
    def __init__(self, page: Page):
        self.page = page

    def login(self, url, username, password):
        self.page.goto(url)

        self.page.wait_for_load_state("networkidle")

        self.page.fill('#username', username)
        self.page.fill('#password', password)
        self.page.click('#submitButtonPL')
        
        try:
            self.page.wait_for_selector('#submitButtonPL', state='detached', timeout=10000)
            print("successfully logged in")
            
        except Exception as e:
            print(f"error while login: {e}")

    def open_test_module(self):
        try:
            self.page.click('text="Unit 1.1"')
        except Exception as e:
            print(f"Didn't find Unit 1.1. error: {e}")
            return

        try:
            launch_selector = 'img[src*="orange_launch"]'
            
            self.page.wait_for_selector(launch_selector, state='visible', timeout=3000)
            self.page.click(launch_selector)
            print("The Launch button is found and pressed")
            
        except Exception:
            print("The Launch button didn't appear (the test opened automatically). Let's continue.")
            
        time.sleep(2)