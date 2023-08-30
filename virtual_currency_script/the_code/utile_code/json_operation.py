import time
import yaml
from my_selenium_wrapper import MySeleniumWrapper
import sys
from selenium.webdriver.common.keys import Keys


def execute_steps_from_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        test_steps = yaml.safe_load(file)
        # print(test_steps)
    selenium_wrapper = MySeleniumWrapper()

    for step in test_steps:
        action = step['action']
        if action == 'open_url':
            selenium_wrapper.open_url(step['url'])
        elif action == 'find_element':
            locator = step['locator']
            selenium_wrapper.find_element(locator)
        elif action == 'send_keys_to_element':
            locator = step['locator']
            selenium_wrapper.send_keys_to_element(locator, step['input_text'])
        elif action == 'click_element':
            locator = step['locator']
            selenium_wrapper.click_element(locator)
        elif action == 'wait_for_element':
            locator = step['locator']
            selenium_wrapper.wait_for_element(locator, timeout=step['timeout'])
        # elif action == 'get_element_text':
        #     text = selenium_wrapper.get_element_text(element)
        #     print(f"元素文本内容: {text}")
        elif action == 'save_screenshot':
            selenium_wrapper.save_screenshot(step['file_path'])
        elif action == 'close_browser':
            selenium_wrapper.close_browser()
        elif action == 'execute_javascript':
            selenium_wrapper.execute_javascript(step['javascript'])
        elif action == 'switch_to_window':
            selenium_wrapper.switch_to_window(int(step['page_index']))
            time.sleep(1)
        elif action == 'clouse_handles':
            selenium_wrapper.clouse_handles()
        elif action == 'switch_to_new_windows':
            selenium_wrapper.switch_to_new_windows()
        elif action == 'shadow_root':
            selenium_wrapper.shadow_root(step['locator'])
            time.sleep(1)
        elif action == 'perform_mouse_action':
            selenium_wrapper.perform_mouse_action(step['x'], step['y'])
        elif action == 'timesleep':
            time.sleep(step['timesleep'])
        elif action == 'refresh_page':
            selenium_wrapper.refresh_page()
        elif action == 'qingkongliulanqishuju':
            selenium_wrapper.qingkongliulanqishuju()
        elif action == 'driver_quit':
            selenium_wrapper.driver_quit()
        else:
            print(f"未知操作: {action}")
        print(f'步骤{step["step"]}:{step["name"]}')

    # while 1:
    #     pass


if __name__ == "__main__":
    arg1 = sys.argv[1]
    execute_steps_from_yaml(arg1)

# if key['steps']['action'] == 'open_url':
#     print('执行登录操作')
# elif key['operation'] == 'search':
#     print('执行其他操作')
# elif key['operation'] == 'click_button':
#     print('执行点击操作')
