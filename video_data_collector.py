from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from logging_config import log_message, log_error, log_warning, log_debug

def collect_video_data(driver, filename="video_data.txt"):
    try:
        # asteapta pana cand box-ul cu informatii este disponibil
        info_panel = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "info-container"))
        )

        # extrage titlul video-ului
        title_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#title h1 yt-formatted-string'))
        )
        title = title_element.text

        # extrage URL-ul video-ului
        video_url = driver.current_url

        # extrage autorul (canalul)
        author_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[1]/ytd-video-owner-renderer/div[1]/ytd-channel-name/div/div/yt-formatted-string/a'))
        )
        author = author_element.text

        # extrage numarul de subscriberi
        subscriber_count_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[1]/ytd-video-owner-renderer/div[1]/yt-formatted-string'))
        )
        subscribers = subscriber_count_element.text

        # extrage numarul de vizualizari
        views = info_panel.find_element(By.CSS_SELECTOR, '#info span[style-target="bold"]').text.split(' ')[0]

        # extrage data publicarii
        publish_date = info_panel.find_elements(By.CSS_SELECTOR, 'span[style-target="bold"]')[2].text.strip()

        # extrage hashtag-urile
        hashtags_elements = info_panel.find_elements(By.CSS_SELECTOR, 'a[style-target="bold"]')
        if hashtags_elements:
            hashtags = [tag.text for tag in hashtags_elements]
        else:
            hashtags = ["N/A"] # scrie N/A daca nu sunt hashtag-uri

            log_message(
                f"Datele video-ului au fost colectate: Titlu: {title}, Vizualizari: {views}, Data: {publish_date}, "
                f"Hashtag-uri: {', '.join(hashtags)}, Autor: {author}, Subscriberi: {subscribers}")

        # scrie datele colectate intr-un fisier
        with open(filename, 'w') as file:
            file.write(f"Titlu: {title}\n")
            file.write(f"URL: {video_url}\n")
            file.write(f"Autor: {author}\n")
            file.write(f"Subscriberi: {subscribers}\n")
            file.write(f"Vizualizari: {views}\n")
            file.write(f"Data publicarii: {publish_date}\n")
            file.write(f"Hashtag-uri: {', '.join(hashtags)}\n")

        log_message(f"Datele video-ului au fost salvate in {filename}")

    except Exception as e:
        log_error(f"Eroare la colectarea datelor video: {e}")
