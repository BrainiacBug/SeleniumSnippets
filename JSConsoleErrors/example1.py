from selenium import webdriver

browser_ff = webdriver.FirefoxProfile()
browser_ff.set_preference("webdriver.log.driver", "SEVERE")
driver = webdriver.Firefox(firefox_profile=browser_ff)

driver.get("file:///C:/path/to/your/file/test.html")
for entry in driver.get_log('browser'):
    if str(entry["level"]) == "SEVERE":
        print entry["message"]

driver.close()
driver.quit()