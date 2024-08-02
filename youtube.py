import json
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login(email, password):
    driver = uc.Chrome(use_subprocess=True)
    wait = WebDriverWait(driver, 30)  

    url_login = 'https://accounts.google.com/AddSession?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den-GB%26next%3D%252F&hl=en-GB&passive=false&service=youtube&uilel=0'
    driver.get(url_login)

    try:
        wait.until(EC.visibility_of_element_located((By.NAME, 'identifier'))).send_keys(email)
        wait.until(EC.element_to_be_clickable((By.ID, 'identifierNext'))).click()
        time.sleep(2)
        wait.until(EC.visibility_of_element_located((By.NAME, 'Passwd'))).send_keys(password)
        wait.until(EC.element_to_be_clickable((By.ID, 'passwordNext'))).click()
        time.sleep(5)
    except Exception as e:
        # print(f"Login gagal {email}: {e}")
        print(f"Login gagal {email}: tidak ditemukan")
        driver.close()
        return None, None

    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "Incorrect password")]')))
        print(f"Password salah {email}")
        driver.close()
        return None, None
    except:
        pass

    print(f"Login sukses untuk {email}")
    return driver, wait

def skip_ads(wait):
    while True:
        try:
            skip_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.ytp-skip-ad-button')))
            skip_button.click()
            print("Skip iklan berhasil")
            time.sleep(1)
        except Exception:
            print("Skip iklan tidak ditemukan")
            break

def interact_with_urls(driver, wait, urls):
    for url_dict in urls:
        url = url_dict['url']
        driver.get(url)
        
        time.sleep(5)

        skip_ads(wait)

        try:
            title_element = driver.find_element(By.CSS_SELECTOR, 'yt-formatted-string.style-scope.ytd-watch-metadata')
            print(f"Judul video: {title_element.text}")
        except Exception as e:
            print("Judul video tidak ditemukan:", e)

        try:
            channel_element = driver.find_element(By.CSS_SELECTOR, 'a.yt-simple-endpoint.style-scope.yt-formatted-string')
            print(f"Channel: {channel_element.text}")
        except Exception as e:
            print(f"Gagal menemukan elemen channel: {e}")

        # Like button
        try:
            time.sleep(10)
            like_buttons = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'yt-animated-icon[animated-icon-type="LIKE"]'))
            )
            
            for like_button in like_buttons:
                button = like_button.find_element(By.XPATH, './ancestor::button')
                aria_pressed = button.get_attribute("aria-pressed")
                if aria_pressed == "false":
                    button.click()
                    time.sleep(2)
                    print("Like video berhasil")
                    break
            else:
                print("Video sudah di-like atau tombol like tidak ditemukan.")
        except Exception as e:
            print(f"Gagal klik like button karena: {e}")

        # Subscribe button
        try:
            subscribe_button_shape = driver.find_element(By.ID, 'subscribe-button-shape')
            if "invisible" not in subscribe_button_shape.get_attribute("class"):
                subscribe_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//ytd-subscribe-button-renderer//button')))
                subscribe_button.click()
                print("Subscribe berhasil")
            else:
                print("Sudah subscribe")
        except Exception as e:
            print("Gagal subscribe button:", e)

        time.sleep(5)

    driver.close()

with open('data.json', 'r') as file:
    credentials_list = json.load(file)

with open('data_url.json', 'r') as file:
    urls = json.load(file)

for credentials in credentials_list:
    email = credentials['email']
    password = credentials['password']
    driver, wait = login(email, password)
    if driver and wait:
        interact_with_urls(driver, wait, urls)