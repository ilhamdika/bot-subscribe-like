import json
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from datetime import datetime
import requests
from dotenv import load_dotenv

load_dotenv()
base_url = os.getenv('BASE_URL')

def create_report_folder():
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    folder_name = f"laporan/like-subscribe-watch/{now}"
    os.makedirs(folder_name, exist_ok=True)
    print(f"Folder laporan dibuat: {folder_name}")
    return folder_name

def save_to_report(folder_name, email, message):
    report_file = os.path.join(folder_name, f"{email}.txt")
    with open(report_file, 'a', encoding='utf-8') as file:
        file.write(f"{datetime.now().strftime('%H:%M:%S')} - {message}\n")
    print(f"{datetime.now().strftime('%H:%M:%S')} - {email}: {message}")

def send_report_to_api(email, username, folder_name, url, report_type="like-subscribe-watch", status_login="success"):
    api_url = f"{base_url}/api/make_report"
    folder_date = os.path.basename(folder_name)

    report_file_path = os.path.join(folder_name, f"{email}.txt")
    with open(report_file_path, 'r', encoding='utf-8') as file:
        keterangan = file.read()

    data = {
        "tipe": report_type,
        "tanggal": folder_date,
        "email": email,
        "username": username,
        "keterangan": keterangan,
        "status_login": status_login,
        "url": url
    }

    try:
        response = requests.post(api_url, data=data)
        print(f"Response status code: {response.status_code}")
        print(f"Response text: {response.text}")
        if response.status_code == 200:
            print(f"Report for {email} successfully sent to API.")
        else:
            print(f"Failed to send report for {email}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending report for {email}: {e}")

def login(email, password, folder_name):
    driver = uc.Chrome(use_subprocess=True)
    wait = WebDriverWait(driver, 10)
    status_login = "success"

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
        save_to_report(folder_name, email, f"Login gagal: tidak ditemukan \n")
        status_login = "failed"
        driver.close()
        return None, None, status_login

    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "Wrong password")]')))
        save_to_report(folder_name, email, "Password salah \n")
        status_login = "failed"
        driver.close()
        return None, None, status_login
    except:
        pass

    try:
        wait.until(EC.visibility_of_element_located((By.ID, 'avatar-btn')))
        save_to_report(folder_name, email, "Login sukses \n")
        return driver, wait, status_login
    except Exception as e:
        save_to_report(folder_name, email, f"Login gagal: waktu tunggu melebihi batas \n")
        status_login = "failed"
        driver.close()
        return None, None, status_login

def skip_ads(wait, folder_name, email):
    while True:
        try:
            skip_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.ytp-skip-ad-button')))
            skip_button.click()
            save_to_report(folder_name, email, "Skip iklan berhasil")
            time.sleep(1)
        except Exception:
            save_to_report(folder_name, email, "Skip iklan tidak ditemukan")
            break

def interact_with_urls(driver, wait, urls, folder_name, email):
    for url_dict in urls:
        url = url_dict['url']
        username = url_dict.get('username')
        driver.get(url)
        
        time.sleep(5)

        skip_ads(wait, folder_name, email)

        try:
            title_element = driver.find_element(By.CSS_SELECTOR, 'div#title yt-formatted-string.style-scope.ytd-watch-metadata')
            save_to_report(folder_name, email, f"Judul video: {title_element.text}")
        except Exception as e:
            save_to_report(folder_name, email, f"Judul video tidak ditemukan: {e}")

        try:
            channel_element = driver.find_element(By.CSS_SELECTOR, 'a.yt-simple-endpoint.style-scope.yt-formatted-string')
            save_to_report(folder_name, email, f"Channel: {channel_element.text}")
        except Exception as e:
            save_to_report(folder_name, email, f"Gagal menemukan elemen channel: {e}")

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
                    save_to_report(folder_name, email, "Like video berhasil")
                    break
            else:
                save_to_report(folder_name, email, "Video sudah di-like atau tombol like tidak ditemukan.")
        except Exception as e:
            save_to_report(folder_name, email, f"Gagal klik like button karena: {e}")

        try:
            subscribe_button_shape = driver.find_element(By.ID, 'subscribe-button-shape')
            if "invisible" not in subscribe_button_shape.get_attribute("class"):
                subscribe_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//ytd-subscribe-button-renderer//button')))
                subscribe_button.click()
                save_to_report(folder_name, email, "Subscribe berhasil \n")
            else:
                save_to_report(folder_name, email, "Sudah subscribe \n")
        except Exception as e:
            save_to_report(folder_name, email, "Sudah subscribe \n")
            # save_to_report(folder_name, email, f"Gagal subscribe button: {e} \n")

        send_report_to_api(email, username, folder_name, url, status_login=status_login)

        time.sleep(5)

    driver.close()

if __name__ == "__main__":
    folder_name = create_report_folder()

    with open('data.json', 'r') as file:
        credentials_list = json.load(file)

    with open('data_url.json', 'r') as file:
        urls = json.load(file)

    for credentials in credentials_list:
        email = credentials['email']
        password = credentials['password']
        driver, wait, status_login = login(email, password, folder_name)
        if driver and wait:
            interact_with_urls(driver, wait, urls, folder_name, email)
        else:
            for url_dict in urls:
                url = url_dict['url']
                username = url_dict.get('username')
                send_report_to_api(email, username, folder_name, url, status_login="failed")
