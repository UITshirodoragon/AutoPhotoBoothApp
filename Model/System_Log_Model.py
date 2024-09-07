import logging
import datetime

# Hướng dẫn sử dụng
'''
Các cấp độ log chuẩn trong Python, từ thấp đến cao về mức độ nghiêm trọng:

DEBUG: Cấp độ thấp nhất, dùng để ghi lại thông tin chi tiết nhất trong quá trình phát triển và gỡ lỗi. 
Thường chứa thông tin chi tiết về trạng thái của ứng dụng.

INFO: Dùng để ghi lại các sự kiện thông thường trong ứng dụng, chẳng hạn như các hành động thành công 
của người dùng hoặc thông tin về các bước quan trọng trong quá trình xử lý.

WARNING: Dùng để ghi lại các cảnh báo về những tình huống bất thường hoặc những hành động không mong muốn 
nhưng không làm gián đoạn ứng dụng.

ERROR: Dùng để ghi lại các lỗi nghiêm trọng, thường là những lỗi mà ứng dụng không thể xử lý được và cần 
được khắc phục.

CRITICAL: Cấp độ cao nhất, dùng để ghi lại các lỗi nghiêm trọng nhất, có thể dẫn đến việc ngừng 
hoạt động của ứng dụng hoặc hệ thống.

Lưu ý:
- module này sẽ tạo duy một file .log duy nhất khi chạy. 
- file sẽ được đặt tên theo thời gian hiện tại

Bước 1: import package và module

import sys
import os

# Đường dẫn tới folder chứa module 
package_controller_path = os.path.abspath(os.path.join('..', 'PhotoBoothApp'))
if package_controller_path not in sys.path:
    sys.path.append(package_controller_path)

from AppController import System_Log_Controller

Bước 2: Tạo đối tượng trong file

logger = logger = System_Log_Controller.SystemLogController(user_id, position)

Có thể truyền vào: user_id là user_001,...
                position là vị trí được ghi. vd: Main_window_interface, Camera_Configuration_Controller,...

Bước 3: sử dụng và ghi log

logger.write_info("Hello")


'''

# Get current time
current_time = datetime.datetime.now()
description = "system_log"

# Format file name with many argruments
file_name = f"Data/SystemLog/{description}_{current_time.strftime('%d%m%Y_%H%M%S')}.log"

# open or create new files
with open(file_name, 'w') as file:
    file.write(f"Created file system log at {current_time.strftime('%H:%M:%S %d/%m/%Y')}. Have a great day!\n")

# class
class SystemLogModel:
    def __init__(self, user_id, position):
        
        self.logger = logging.getLogger(user_id + " - "+ position)
        self.logger.setLevel(logging.DEBUG)

        # Create file handler which logs even debug messages
        file_handle = logging.FileHandler(file_name)
        file_handle.setLevel(logging.DEBUG)

        # Create formatter and add it to the handlers
        formatter = logging.Formatter('[%(asctime)s] - [%(levelname)s] - %(name)s: %(message)s')
        file_handle.setFormatter(formatter)

        # Add the handlers to the logger
        self.logger.addHandler(file_handle)

    # write log message at level infomation
    '''
    INFO: Dùng để ghi lại các sự kiện thông thường trong ứng dụng, chẳng hạn như các hành động thành công 
    của người dùng hoặc thông tin về các bước quan trọng trong quá trình xử lý.
    '''
    def write_info(self, message):
        self.logger.info(message)
        
    # write log message at level warning
    '''
    WARNING: Dùng để ghi lại các cảnh báo về những tình huống bất thường hoặc những hành động không 
    mong muốn nhưng không làm gián đoạn ứng dụng.
    '''
    # 
    def write_warning(self, message):
        self.logger.warning(message)

    # write log message at level error
    '''
    ERROR: Dùng để ghi lại các lỗi nghiêm trọng, thường là những lỗi mà ứng dụng không thể xử lý 
    được và cần được khắc phục.
    '''
    def write_error(self, message):
        self.logger.error(message)

    # write log message at level debug
    '''
    DEBUG: Cấp độ thấp nhất, dùng để ghi lại thông tin chi tiết nhất trong quá trình phát triển và gỡ lỗi. 
    Thường chứa thông tin chi tiết về trạng thái của ứng dụng.
    '''
    def write_debug(self, message):
        self.logger.debug(message)
        
    # write log message at level debug
    '''
    CRITICAL: Cấp độ cao nhất, dùng để ghi lại các lỗi nghiêm trọng nhất, có thể dẫn đến việc ngừng 
    hoạt động của ứng dụng hoặc hệ thống.
    '''
    def write_critical(self, message):
        self.logger.critical(message)
        
    # write log message at level error, warning with eception
    '''
    Cho phép ghi lại lỗi exception vào file log
    '''
    def write_excetption(self, message):
        self.logger.exception(message)
    
    # write log message at level default debug
    '''
    Cho phép ghi log với leve mặc định
    '''
    def write_log(self, message):
        self.logger.log(message)

