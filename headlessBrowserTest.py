import time
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait

command_list = ['t!credits', 't!cat', 't!catfacts', 't!pet train', 't!dog', 't!dogfacts', 't!8ball is Matt the dumbest boy in all the land?', 't!pet train', 't!roll d20', 't!rps rock', 't!color red', 't!color green', 't!color blue', 't!pet train', 't!numberfacts', 't!fortune', 't!choose cat | dog', 't!credits', 't!pet', 't!pet train', 't!pet clean', 't!pet play', 't!pet feed', 't!rank']

options = Options()
options.add_argument('-headless')
browser = Firefox(executable_path='geckodriver', firefox_options=options)
wait = WebDriverWait(browser, timeout=10)
browser.get('https://discordapp.com/channels/419703147292917771/472076197925486602')

email_button = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div/form/div/div[3]/div[1]/div/input")
email_button.send_keys('your@email.com')
password_button = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div/form/div/div[3]/div[2]/div/input")
password_button.send_keys('yourPassword')
login_button = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div/form/div/div[3]/button[2]")
login_button.click()
time.sleep(10)
disclaimer_button = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[5]/button[2]').click()
time.sleep(5)
assert '#spam' in browser.title
text_field = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/form/div/div/textarea")

while True:
    for i in command_list:
        text_field.send_keys("{}".format(i), Keys.RETURN)
        time.sleep(6)