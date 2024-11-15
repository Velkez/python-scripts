import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class example(unittest.TestCase):
    
    def test(self):
        driver = webdriver.Chrome()
        path = "https://www.youtube.com/watch?v=jZy_UfkWIxU"
        seconds = 0
        
        driver.get(f"{path}")
        time.sleep(1)
        
        minutes = driver.find_element(By.CLASS_NAME, "ytp-time-duration")
        print (minutes)
        
        try:
            play = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "movie_player"))
            )
            play.click()
        except Exception as e:
            print(f"No se puedo encontrar el enlace: {e}")
        
        time.sleep(10)


if __name__ == '__main__':
    unittest.main()