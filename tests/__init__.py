from selenium import webdriver
self.browserSession = webdriver.Chrome()
self.browserSession.get("https://www.youtube.com/watch?v=wJRZkY2m_fg")
self.browserSession.find_element("Submit").click()
self.browserSession.title()