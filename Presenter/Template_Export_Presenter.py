from __future__ import annotations
from typing import Protocol

from PyQt5.QtWidgets import QStackedWidget, QWidget, QVBoxLayout, QScrollArea, QLabel, QPushButton, QProgressBar
from PyQt5.QtCore import pyqtSignal, QThread, QTimer, QTime 


from View.Template_Export_View import TemplateExportView

from Model.Template_Export_Model import TemplateExportModel, TemplateExportWorker
from Model.User_Model import UserModel, User
from Model.Template_Model import TemplateModel
from Model.Google_Drive_Model import GoogleDriveModel
from Model.Image_Model import ImageModel

from Presenter.Mediator import IMediator, ConcreteMediator

class TemplateExportPresenter:
    
    
    
    def __init__(self, model: TemplateExportModel, 
                 view: TemplateExportView, 
                 stack_view: QStackedWidget, 
                 user_control_model: UserModel, 
                 template_control_model: TemplateModel,
                 google_drive_model: GoogleDriveModel,
                 image_control_model: ImageModel) -> None:
        self.model = model
        self.view = view
        self.stack_view = stack_view
        self.user_control_model = user_control_model
        self.template_control_model = template_control_model
        self.google_drive_model = google_drive_model
        self.image_control_model = image_control_model
        self.mediator = None
        
        self.view.TEV_back_button_signal.connect(self.handle_back_button_clicked)
        self.view.TEV_restart_button_signal.connect(self.handle_restart_button_clicked)
        
        self.template_export_worker = None
        
        self.is_update_final_template_with_images_finished = False
        
        self.minute = 1
        self.second = 30
        self.qr_code_countdown_initial_time = QTime(0, self.minute, self.second)
        self.qr_code_countdown_time = QTime(0, self.minute, self.second)
        
        self.qr_code_countdown_timer = QTimer()
        self.qr_code_countdown_timer.timeout.connect(self.handle_udpate_qr_code_countdown_timer)
        
        # self.template_export_worker.finished.connect(self.handle_finish_template_export_worker)
        
        
    def handle_start_qr_code_countdown_timer(self) -> None:
        self.qr_code_countdown_timer.start(1000)
        
    def handle_reset_qr_code_countdown_timer(self) -> None:
        self.qr_code_countdown_time = QTime(0, self.minute, self.second)
        self.view.update_scan_text_label_gui('Scanning QR code to download in: '+ self.qr_code_countdown_time.toString('mm:ss'))
      
    def handle_udpate_qr_code_countdown_timer(self) -> None:
        self.qr_code_countdown_time = self.qr_code_countdown_time.addSecs(-1)
        self.view.update_scan_text_label_gui('Scanning QR code to download in: '+ self.qr_code_countdown_time.toString('mm:ss'))
        if self.qr_code_countdown_time == QTime(0, 0, 0):
            self.handle_restart_button_clicked()
        
        
        
    def handle_start_template_export_worker(self) -> None:
        self.template_export_worker = TemplateExportWorker(self.model, 
                                                           self.google_drive_model,
                                                            self.template_control_model.get_template_from_database(self.template_control_model.selected_template_id), 
                                                            self.user_control_model.get_user())
        
        self.template_export_worker.TEW_progress_signal.connect(self.view.update_process_export_final_template_progress_bar_gui)
        self.template_export_worker.TEW_finished_signal.connect(self.handle_finish_template_export_worker)
        
        
        # self.view.TEV_process_bar_value_signal.connect(self.handle_processing_template_export_worker)
        
        # self.template_export_worker.run = self.model.export_template_with_images(self.template_control_model.get_template_from_database(self.template_control_model.selected_template_id), 
        #                                                                          self.user_control_model.get_user(), 
        #                                                                          self.view.TEV_process_bar_value_signal.emit)
        
        self.template_export_worker.start()
    
    def handle_finish_template_export_worker(self) -> None:
        print('finish')
        if not self.is_update_final_template_with_images_finished:
            self.handle_reset_qr_code_countdown_timer()
            self.handle_start_qr_code_countdown_timer()
            self.is_update_final_template_with_images_finished = True
            self.template_export_worker.quit()
            self.view.show_all_widgets()
            self.view.update_final_template_with_images_gui(self.user_control_model.get_user().gallery_folder_path + f'/final_user_{self.user_control_model.get_user().id}.png')
            self.view.update_qr_code_image_gui(self.user_control_model.get_user().gallery_folder_path + f'/qr_code_google_drive_user_{self.user_control_model.get_user().id}.png')
            
    def set_mediator(self, mediator: IMediator) -> None:
        self.mediator = mediator    
    
    def handle_back_button_clicked(self) -> None:
        self.qr_code_countdown_timer.stop()
        self.handle_reset_qr_code_countdown_timer()
        self.qr_code_countdown_timer.stop()
        self.mediator.notify('template_export_presenter', 'image_capture_presenter', 'start_preview_process')
        self.stack_view.setCurrentIndex(2)
        print(self.template_control_model.selected_template_id)
        self.is_update_final_template_with_images_finished = False
        
    def handle_restart_button_clicked(self) -> None:
        self.qr_code_countdown_timer.stop()
        self.handle_reset_qr_code_countdown_timer()
        self.stack_view.setCurrentIndex(0)
        self.user_control_model.delete_user()
        self.user_control_model.disable_user()
        self.user_control_model.get_user().image_count = 0
        self.is_update_final_template_with_images_finished = False
        if self.mediator:
            self.mediator.notify('template_export_presenter', 'image_capture_presenter', 'clear_image_gallery_label')
    
    def handle_update_final_template_with_images(self) -> None:
        self.view.hide_all_widgets()
        self.handle_start_template_export_worker()
        # self.model.export_template_with_images(self.template_control_model.get_template_from_database(self.template_control_model.selected_template_id), self.user_control_model.get_user())
    
    # def handle_processing_template_export_worker(self, value) -> None:
    #     print(value)
    #     self.view.update_process_export_final_template_progress_bar_gui(value)
    #     if value == 101:
    #         if not self.is_update_final_template_with_images_finished:
    #             self.is_update_final_template_with_images_finished = True
    #             self.handle_finish_template_export_worker()
