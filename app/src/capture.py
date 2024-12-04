# capture.py

from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from datetime import datetime

def take_capture(config):
    # Kiểm tra và tạo thư mục 'images' nếu chưa tồn tại
    if not os.path.exists('images'):
        os.makedirs('images')

    # Cấu hình cho Selenium WebDriver
    options = Options()
    # options.add_argument('--headless')  # Chạy trình duyệt ở chế độ không hiển thị (không mở cửa sổ trình duyệt)
    options.add_argument("--no-sandbox") # Vô hiệu hóa chế độ sandbox của Chrome.
    options.add_argument("--disable-dev-shm-usage") # Sử dụng ổ đĩa thay vì /dev/shm cho bộ nhớ tạm.
    #options.add_argument("--disable-gpu") # Vô hiệu hóa GPU. Cần thiết khi chạy Chrome headless trên một số hệ thống.
    #options.add_argument("--disable-extensions") # Vô hiệu hóa các tiện ích mở rộng (extensions) của Chrome.
    #options.add_argument("--disable-notifications") # Vô hiệu hóa thông báo từ trang web
    options.add_argument("--start-maximized") # Mở trình duyệt ở chế độ toàn màn hình.
    #options.add_argument("--disable-popup-blocking") # Vô hiệu hóa chặn popup.
    options.add_argument("--window-size=1920,12000") # Đặt kích thước cửa sổ trình duyệt.

    # SELENIUM_REMOTE_URL = f"http://selenium:4444/wd/hub"
    SELENIUM_REMOTE_URL = config['options']['SELENIUM_REMOTE_URL']

    # Đường dẫn tới chromedriver (thay đổi đường dẫn cho phù hợp)
    # service = Service(executable_path='/path/to/chromedriver')

    # driver = webdriver.Chrome(service=service, options=options)
    # Khởi động trình duyệt và kết nối với Selenium server trong Docker
    driver = webdriver.Remote(
        command_executor=SELENIUM_REMOTE_URL,
        options=options
    )

    # Chrome on your desktop
    # driver = webdriver.Chrome(options=chrome_options)
    # driver.set_window_size(1920, 1080)  # Điều chỉnh kích thước cửa sổ trình duyệt nếu cần

    try:
        # Truy cập trang coingecko.com
        driver.get(config['options']['CAPTURE_URL']) # CAPTURE_URL=https://www.coingecko.com

        # Chờ trang web tải xong
        time.sleep(5)  # Điều chỉnh thời gian nếu cần thiết

        # Lấy thời gian hiện tại UTC để đặt tên tệp
        now = datetime.utcnow()
        timestamp = now.strftime('%Y-%m-%d_%H-%M-%S')

        # Đặt tên tệp ảnh chụp màn hình
        screenshot_filename = f'images/coingecko_{timestamp}.png'
        
        # Tìm thẻ table
        # table = driver.find_element(By.XPATH, "//table[@data-coin-table-target='table']")
        
        # Chụp màn hình và lưu lại
        driver.save_screenshot(screenshot_filename)

        # Chụp hình thẻ table và lưu vào file
        # table.screenshot(screenshot_filename)
        
        print(f'Đã lưu ảnh chụp màn hình vào {screenshot_filename}')

    finally:
        driver.quit()