###2021年问卷###
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import schedule
import time

def auto2():
    chromeOptions = webdriver.ChromeOptions()
    browser = webdriver.Chrome(options=chromeOptions)
    wait = WebDriverWait(browser, 10)
    browser.get('https://jinshuju.net/f/kDiOo6')  # 问卷网址

    # 姓名
    name_input = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="root"]/div/form/div[3]/div[1]/div[2]/div/div/div[2]/div[1]/div/span/span/input')))
    name_input.clear()
    name_input.send_keys('林小惟')  # 在这写入你的姓名


    sid_input = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="root"]/div/form/div[3]/div[1]/div[4]/div/div/div[2]/div[1]/div/span/input')))
    sid_input.clear()
    sid_input.send_keys('202122011004')  # 在这写入你的学号


    stu_type = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@value="KsBW"]')))  # 全日制
    stu_type.click()

    live_pos = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@value="JsBh"]')))  # 校内宿舍
    live_pos.click()

    # 选择校区
    scholName = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@value="zBCK"]')))  # 清水河
    scholName.click()

    home_time = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@value="GaXt"]')))  # 11点前
    home_time.click()

    position = wait.until(EC.presence_of_element_located((By.XPATH,
                                                        '//*[@class="ant-btn ant-btn-primary ant-btn-block sc-jRQBWg elvOuI geo-filed__caller form-theme--general-button"]')))
    position.click()

    position_input = wait.until(EC.presence_of_element_located((By.XPATH,
                                                          '//*[@id="root"]/div/form/div[3]/div[1]/div[14]/div/div/div[2]/div[1]/div/span/div/div/div[2]/div[2]/div/input')))
    position_input.clear()
    position_input.send_keys('电子科技大学清水河')
    time.sleep(1)
    position = wait.until(EC.presence_of_element_located((By.XPATH,
                                                          '//*[@class="ant-btn sc-jRQBWg elvOuI search-btn"]')))
    position.click()


    vacation = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@value="srmW"]')))  # 非请假学生
    vacation.click()

    submit = wait.until(EC.presence_of_element_located((By.XPATH,
                                                          '//*[@class="ant-btn ant-btn-primary sc-jRQBWg elvOuI published-form__submit form-theme--submit-button"]')))
    submit.click()

    # 关闭网页
    browser.quit()

# 问卷自动填写：
def auto():
    chromeOptions = webdriver.ChromeOptions()
    browser = webdriver.Chrome(options=chromeOptions)
    wait = WebDriverWait(browser, 10)
    browser.get('https://jinshuju.net/f/kDiOo6')  # 问卷网址

    # 姓名
    name_input = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="root"]/div/form/div[3]/div[1]/div[2]/div/div/div[2]/div[1]/div/span/span/input')))
    name_input.clear()
    name_input.send_keys('白若明')  # 在这写入你的姓名


    sid_input = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="root"]/div/form/div[3]/div[1]/div[4]/div/div/div[2]/div[1]/div/span/input')))
    sid_input.clear()
    sid_input.send_keys('202121010241')  # 在这写入你的学号


    stu_type = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@value="KsBW"]')))  # 全日制
    stu_type.click()

    live_pos = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@value="JsBh"]')))  # 校内宿舍
    live_pos.click()

    # 选择校区
    scholName = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@value="zBCK"]')))  # 清水河
    scholName.click()

    home_time = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@value="GaXt"]')))  # 11点前
    home_time.click()

    position = wait.until(EC.presence_of_element_located((By.XPATH,
                                                        '//*[@class="ant-btn ant-btn-primary ant-btn-block sc-jRQBWg elvOuI geo-filed__caller form-theme--general-button"]')))
    position.click()

    position_input = wait.until(EC.presence_of_element_located((By.XPATH,
                                                          '//*[@id="root"]/div/form/div[3]/div[1]/div[14]/div/div/div[2]/div[1]/div/span/div/div/div[2]/div[2]/div/input')))
    position_input.clear()
    position_input.send_keys('电子科技大学清水河')
    time.sleep(1)
    position = wait.until(EC.presence_of_element_located((By.XPATH,
                                                          '//*[@class="ant-btn sc-jRQBWg elvOuI search-btn"]')))
    position.click()


    vacation = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@value="srmW"]')))  # 非请假学生
    vacation.click()

    submit = wait.until(EC.presence_of_element_located((By.XPATH,
                                                          '//*[@class="ant-btn ant-btn-primary sc-jRQBWg elvOuI published-form__submit form-theme--submit-button"]')))
    submit.click()

    # 关闭网页
    browser.quit()


# 定时功能：
schedule.every().day.at("20:40").do(auto)
schedule.every().day.at("20:37").do(auto2)


# while True:
#     schedule.run_pending()
#     time.sleep(1)

if __name__ == "__main__":
    auto()



