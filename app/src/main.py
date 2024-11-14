# main.py

import time
from capture import take_capture
import configparser
import argparse
import schedule
import pytz

def load_config():
    # Tạo parser cho các tham số dòng lệnh
    parser = argparse.ArgumentParser(description='Ứng dụng đọc cấu hình')
    parser.add_argument('-c', '--config', type=str, default='app.conf',
                        help='Đường dẫn tới tệp cấu hình')

    args = parser.parse_args()

    config_file = args.config

    # Tạo một đối tượng ConfigParser
    config = configparser.ConfigParser()
    
    # Đọc tệp cấu hình
    config.read(config_file)
    
    return config

def worker(name, delay):
    """Thread worker function."""
    print(f"Thread {name} starting")

def task():
    print('Doing Task...')
    # Gọi một đối tượng ConfigParser
    config = load_config()
    take_capture(config)

def main():
    # Gọi một đối tượng ConfigParser
    config = load_config()
    take_capture(config)



# Định nghĩa múi giờ UTC
timezone = pytz.timezone('UTC')
schedule.every().day.at("00:00").do(task)

if __name__ == "__main__":
    print('Coin Market Capture')
    main()

    # take_capture()
    # Loop : Vòng lặp chạy tác vụ
    while True:
        schedule.run_pending()
        time.sleep(100) # 10 seconds

