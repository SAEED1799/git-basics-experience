# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# class Youtube_Page_Test_Speed_Video:
#     SPEED_VIDEO = "//a[@id='video-title']]"
#     def __init__(self, driver):
#         self.driver = driver
#
#     def search_and_select_video(self):
#         search_box = self.driver.find_element(By.XPATH, self.SPEED_VIDEO)
#         search_box.send_keys()
#         # search_box.submit()
#         # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,self.SPEED_VIDEO))).click()
#         # time.sleep(5)  # Wait for video player to load
#
#     def change_playback_speed(self, speed):
#         settings_button = self.driver.find_element(By.CLASS_NAME, "ytp-settings-button")
#         settings_button.click()
#         playback_speed_option = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Playback speed')]")
#         playback_speed_option.click()
#         speed_option = self.driver.find_element(By.XPATH, f"//div[contains(text(), '{speed}')]")
#         speed_option.click()
#         time.sleep(2)  # Wait for playback speed to change
#
#     def get_current_playback_speed(self):
#         return self.driver.execute_script("return document.querySelector('.video-stream').playbackRate")
