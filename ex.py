from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Firefox profilinizin dizin yolunu ve profil adını belirtin
profile_path = "/root/.mozilla/firefox/dlr2maa5.default-release"

# Firefox profilini oluşturun
firefox_profile = webdriver.FirefoxProfile(profile_path)

# WebDriver'ı başlatırken profilinizi kullanın
options = webdriver.FirefoxOptions()
options.profile = firefox_profile
driver = webdriver.Firefox(options=options)

# YouTube kanalına gidin
driver.get("https://www.youtube.com/@mahperest/videos")
time.sleep(10)  # Sayfanın yüklenmesini beklemek için birkaç saniye bekleyin

# Sayfada "Pubg" isimli videoları açın
video_elements = driver.find_elements(By.XPATH, "//a[contains(@title, 'Pubg')]")
for video_element in video_elements:
    video_url = video_element.get_attribute("href")
    driver.execute_script("window.open(arguments[0], '_blank');", video_url)

# Selenium çalışmasını kapatın
