from playwright.sync_api import sync_playwright
import config
from core.lms_driver import LmsDriver

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        bot = LmsDriver(page)

        bot.login(config.LOGIN_URL, config.LOGIN, config.PASSWORD)

        bot.open_test_module()

        input("Press Enter to close the browser:")
        
        browser.close()

if __name__ == "__main__":
    main()