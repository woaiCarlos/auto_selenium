from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class MySeleniumWrapper:
    def __init__(self, browser='chrome'):
        if browser.lower() == 'chrome':
            chrome_options = Options()
            # chrome_options.add_argument('--incognito')
            chrome_options.add_extension("/Users/carlos/pythonworkspace/virtual_currency_script/the_code/utile_code/metamask-10.20.0.crx")
            chrome_options.binary_location = r'/Applications/Chromium.app/Contents/MacOS/Chromium'
            chrome_driver_path = r'/Applications/Chromium.app/Contents/MacOS/chromedriver'
            service = Service(chrome_driver_path)
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            self.driver.maximize_window()


        elif browser.lower() == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser.lower() == 'edge':
            self.driver = webdriver.Edge()
        elif browser.lower() == 'safari':
            self.driver = webdriver.Safari()
        elif browser.lower() == 'ie':
            self.driver = webdriver.Ie()
        else:
            raise ValueError("Unsupported browser. Please choose from 'chrome', 'firefox', 'edge', 'safari', or 'ie'.")

    def open_url(self, url):
        self.driver.get(url)

    def go_back(self):
        self.driver.back()

    def go_forward(self):
        self.driver.forward()

    def refresh_page(self):
        self.driver.refresh()

    def find_element(self, locator, input_text=None):
        if locator['type'] == 'id':
            return self.driver.find_element(By.ID, locator['value'])
        elif locator['type'] == 'name':
            return self.driver.find_element(By.NAME, locator['value'])
        elif locator['type'] == 'xpath':
            return self.driver.find_element(By.XPATH, locator['value'])
        elif locator['type'] == 'css_selector':
            return self.driver.find_element(By.CSS_SELECTOR, locator['value'])
        elif locator['type'] == 'tag_name':
            return self.driver.find_element(By.TAG_NAME, locator['value'])
        elif locator['type'] == 'class_name':
            return self.driver.find_element(By.CLASS_NAME, locator['value'])
        elif locator['type'] == 'link_text':
            return self.driver.find_element(By.LINK_TEXT, locator['value'])
        elif locator['type'] == 'partial_link_text':
            return self.driver.find_element(By.PARTIAL_LINK_TEXT, locator['value'])
        else:
            raise ValueError(
                "Unsupported locator type. Please use 'id', 'name', 'xpath', 'css_selector', 'tag_name', 'class_name', 'link_text', or 'partial_link_text'.")

    def send_keys_to_element(self, locator, input_text):
        if locator['type'] == 'id':
            element = self.driver.find_element(By.ID, locator['value'])
            element.send_keys(input_text)
        elif locator['type'] == 'name':
            element = self.driver.find_element(By.NAME, locator['value'])
            element.send_keys(input_text)
        elif locator['type'] == 'xpath':
            element = self.driver.find_element(By.XPATH, locator['value'])
            element.send_keys(input_text)
        elif locator['type'] == 'css_selector':
            element = self.driver.find_element(By.CSS_SELECTOR, locator['value'])
            element.send_keys(input_text)
        elif locator['type'] == 'tag_name':
            element = self.driver.find_element(By.TAG_NAME, locator['value'])
            element.send_keys(input_text)
        elif locator['type'] == 'class_name':
            element = self.driver.find_element(By.CLASS_NAME, locator['value'])
            element.send_keys(input_text)
        elif locator['type'] == 'link_text':
            element = self.driver.find_element(By.LINK_TEXT, locator['value'])
            element.send_keys(input_text)
        elif locator['type'] == 'partial_link_text':
            element = self.driver.find_element(By.PARTIAL_LINK_TEXT, locator['value'])
            element.send_keys(input_text)

    def click_element(self, locator):
        if locator['type'] == 'id':
            element = self.driver.find_element(By.ID, locator['value'])
            element.click()
        elif locator['type'] == 'name':
            element = self.driver.find_element(By.NAME, locator['value'])
            element.click()
        elif locator['type'] == 'xpath':
            element = self.driver.find_element(By.XPATH, locator['value'])
            element.click()
        elif locator['type'] == 'css_selector':
            element = self.driver.find_element(By.CSS_SELECTOR, locator['value'])
            element.click()
        elif locator['type'] == 'tag_name':
            element = self.driver.find_element(By.TAG_NAME, locator['value'])
            element.click()
        elif locator['type'] == 'class_name':
            element = self.driver.find_element(By.CLASS_NAME, locator['value'])
            element.click()
        elif locator['type'] == 'link_text':
            element = self.driver.find_element(By.LINK_TEXT, locator['value'])
            element.click()
        elif locator['type'] == 'partial_link_text':
            element = self.driver.find_element(By.PARTIAL_LINK_TEXT, locator['value'])
            element.click()

    def clear_element(self, element):
        element.clear()

    def get_element_text(self, element):
        return element.text

    def get_element_attribute(self, element, attribute_name):
        return element.get_attribute(attribute_name)

    def switch_to_window(self, index):
        handles = self.driver.window_handles
        print(handles)
        self.driver.switch_to.window(handles[index])
        # self.driver.switch_to.window(current_window_handle)

    def switch_to_new_windows(self):
        handles = self.driver.window_handles
        # 切换到最后一个标签页
        last_handle = handles[-1]
        self.driver.switch_to.window(last_handle)
        print(self.driver.title)
        # # 获取所有窗口句柄
        # all_window_handles = self.driver.window_handles
        # # 切换到新窗口
        # new_window_handle = None
        # for handle in all_window_handles:
        #     if handle != self.driver.current_window_handle:
        #         new_window_handle = handle
        #         break
        # self.driver.switch_to.window(new_window_handle)

    def switch_to_frame(self, frame_reference):
        self.driver.switch_to.frame(frame_reference)

    def execute_javascript(self, script):
        self.driver.execute_script(script)

    def save_screenshot(self, file_path):
        self.driver.save_screenshot(file_path)

    def perform_mouse_action(self, x_offset, y_offset):
        actions = ActionChains(self.driver)
        actions.move_by_offset(x_offset, y_offset).click().perform()

    def perform_keyboard_action(self):
        return self.driver.switch_to

    def implicitly_wait(self, seconds):
        self.driver.implicitly_wait(seconds)

    def wait_for_element(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        if locator['type'] == 'xpath':
            return wait.until(EC.presence_of_element_located((By.XPATH, locator['value'])))
        if locator['type'] == 'css':
            return wait.until(EC.presence_of_element_located((By.CLASS_NAME, locator['value'])))
        if locator['type'] == 'tobeclick':
            wait.until(
                EC.element_to_be_clickable((By.XPATH, locator['value'])))

    def shadow_root(self, locator):
        def expand_shadow_element(element):
            shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', element)
            return shadow_root

        outer = expand_shadow_element(self.driver.find_element(By.XPATH, locator['value']))
        inner = outer.find_element(By.CLASS_NAME, locator['shadow_value'])
        inner.click()

    def qingkongliulanqishuju(self):
        self.driver.get('chrome://settings/clearBrowserData')
        self.driver.find_element(By.XPATH, '//settings-ui').send_keys(Keys.ENTER)
        # onboard_element = self.driver.execute_script("return document.querySelector('onboard-v2');")
        # shadow_root = self.driver.execute_script("return arguments[0].shadowRoot;", onboard_element)
        # shadow_element = shadow_root.find_element(By.XPATH, locator['shadow_value'])
        # shadow_element.click()

    def driver_quit(self):
        self.driver.quit()

    def clouse_handles(self):
        self.driver.close()

    def close_browser(self):
        self.driver.quit()
