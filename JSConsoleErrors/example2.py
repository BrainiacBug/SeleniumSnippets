from selenium import webdriver

browser_ff = webdriver.FirefoxProfile()
browser_ff.add_extension("JSErrorCollector.xpi")
driver = webdriver.Firefox(firefox_profile=browser_ff)

driver.get("file:///C:/path/to/your/file/test.html")
print driver.execute_script('return window.JSErrorCollector_errors.pump()')

driver.close()
driver.quit()