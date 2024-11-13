from __future__ import annotations
from PyQt5.QtCore import QTimer, Qt, QPropertyAnimation, QSequentialAnimationGroup
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QStackedWidget, QLabel, QHBoxLayout, QGraphicsOpacityEffect


from Model.Image_Capture_Model import ImageCaptureModel
from Model.User_Model import UserModel, User
from Model.Template_Model import TemplateModel
from Model.Image_Model import ImageModel
from Model.Template_Export_Model import TemplateExportModel

from Presenter.Mediator import IMediator, ConcreteMediator

from View.Image_Capture_View import ImageCaptureView

from typing import Protocol
from cv2.typing import MatLike


class ImageCapturePresenter:
    def __init__(self, model: ImageCaptureModel,
                 view: ImageCaptureView,
                 stack_view: QStackedWidget,
                 user_control_model: UserModel,
                template_control_model: TemplateModel,
                image_control_model: ImageModel,
                template_export_model: TemplateExportModel
                 ) -> None:
        self.view = view
        self.model = model
        self.stack_view = stack_view
        self.user_control_model = user_control_model
        self.template_control_model = template_control_model
        self.image_control_model = image_control_model
        self.template_export_model = template_export_model
        self.mediator = None
        
        # Khởi động camera trong model
        # self.model.start_preview_process()
        
        
        self.current_index = 1
        self.small_image_labels: list[QLabel] = []
        self.start_pos = None
        self.selected_image_id = 1
        self.touch_event: str = "Touch"
        
        
        self.time_left = 5
        self.countdown_time = self.time_left
        
        self.deleted_image_indexes: list[int] = []

        # Thiết lập QTimer để cập nhật frame liên tục
        self.frame_update_timer = QTimer()
        self.frame_update_timer.timeout.connect(self.handle_update_preview_image)
        self.frame_update_timer.timeout.connect(self.handle_update_preview_fps)
        self.frame_update_timer.start(10)
        
        self.view.ICV_back_button_signal.connect(self.handle_back_button_clicked)
        self.view.ICV_next_button_signal.connect(self.handle_next_button_clicked)
        self.view.ICV_capture_button_signal.connect(self.handle_capture_button_clicked)

    def handle_start_countdown(self):
        self.countdown_timer = QTimer()
        self.countdown_timer.timeout.connect(self.handle_update_countdown)
        self.countdown_timer.start(1000)
        self.view.capture_button.setEnabled(False)  # Disable the button

    def handle_update_countdown(self):
        if self.time_left > 0:
            self.view.update_countdown_number_label_gui(f"View/Icon/number_{self.time_left}_icon.png")
            self.view.animate_countdown_number_label_gui()
            self.time_left -= 1
        else:
            self.countdown_timer.stop()
            self.time_left = self.countdown_time
            self.view.countdown_number_label.clear()
            # self.deleted_image_indexes.sort()
            if self.deleted_image_indexes:
                self.hanđle_restart_capture_and_save_and_update_image_gallery(self.deleted_image_indexes.pop(0))
            else:
                self.handle_capture_and_save_and_update_image_gallery()
            
            # self.mediator.notify(sender = 'image_capture_presenter', receiver = 'template_image_preview_presenter', event = 'update_raw_image', data = {'selected_image_id': self.user_control_model.get_user().image_count})
                    
            # self.mediator.notify(sender = 'image_capture_presenter', receiver = 'template_image_preview_presenter', event = 'update_template_with_a_image', data = {'selected_image_id': self.user_control_model.get_user().image_count})

            self.mediator.notify(sender = 'image_capture_presenter', receiver = 'template_image_preview_presenter', event = 'start_preview_countdown')
            
            self.stack_view.setCurrentIndex(4)
            # self.handle_capture_button_clicked()
            # self.view.capture_button.setEnabled(True)  # Enable the button
    

    
    def set_mediator(self, mediator: IMediator) -> None:
        self.mediator = mediator


    def handle_back_button_clicked(self) -> None:
        # when user change their mind
        if self.view.show_dialog_alert_to_clear_image_gallery():
            self.user_control_model.delete_user_image_gallery(self.user_control_model.get_user())
            self.user_control_model.create_user_image_gallery()
            self.user_control_model.get_user().image_count = 0
            self.handle_clear_image_gallery_label()
            self.image_control_model.create_table_in_database()
            self.deleted_image_indexes.clear()
            self.stack_view.setCurrentIndex(1)
        else:
            pass
        
    def handle_next_button_clicked(self) -> None:
        # self.stack_view.setCurrentIndex(3) 
        self.frame_update_timer.stop()
        if self.user_control_model.get_user().image_count == self.template_control_model.get_template_with_field_from_database(self.template_control_model.selected_template_id, 'number_of_images'):
            self.mediator.notify(sender = 'image_capture_presenter', receiver = 'template_export_presenter', event = 'update_final_template_with_images')
        self.stack_view.setCurrentIndex(3)

        
    def handle_capture_button_clicked(self) -> None:
        print 
        if self.user_control_model.get_user().image_count < self.template_control_model.get_template_with_field_from_database(self.template_control_model.selected_template_id, 'number_of_images'):
            
            self.handle_start_countdown()
            # image_capture_timer = QTimer()
            # image_capture_timer.singleShot(self.countdown_time * 1000 + 500, self.handle_capture_and_save_and_update_image_gallery)
        
        else:  
            self.view.capture_button.setEnabled(True)
            
            # self.frame_update_timer.stop()
            
            # self.stack_view.setCurrentIndex(3)
            # self.mediator.notify(sender = 'image_capture_presenter', receiver = 'template_export_presenter', event = 'update_final_template_with_images')
            
   
    def handle_capture_and_save_and_update_image_gallery(self):
        print(self.user_control_model.get_user().gallery_folder_path)
        if self.user_control_model.get_user().image_count < self.template_control_model.get_template_with_field_from_database(self.template_control_model.selected_template_id,'number_of_images'):
            # self.model.capture_signal_queue.put(obj = self.user_control_model.get_user().gallery_folder_path)
            # self.model.image_captured_count.put(obj = self.user_control_model.get_user().image_count)
            # self.model.number_of_images.put(obj = self.template_control_model.get_template_with_field_from_database(self.template_control_model.selected_template_id, 'number_of_images'))
            self.model.capture_image(user_image_gallery_folder_path = self.user_control_model.get_user().gallery_folder_path,
                                     image_captured_count = self.user_control_model.get_user().image_count)
            # print(self.image_control_model.database_path)
            self.image_control_model.insert_image_into_database(f"image{self.user_control_model.get_user().image_count}.png",
                                                                self.user_control_model.get_user().gallery_folder_path + f"/image{self.user_control_model.get_user().image_count}.png",
                                                                (2592,1944),
                                                                self.user_control_model.get_user().gallery_folder_path + f"/template_with_image{self.user_control_model.get_user().image_count}.png"
                                                                )
            
            self.template_export_model.export_template_with_a_image(self.template_control_model.get_template_from_database(self.template_control_model.selected_template_id),
                                                                    self.image_control_model.get_image_from_database(self.user_control_model.get_user().image_count + 1),
                                                                    None,
                                                                    None)
            
            image_gallery_update_timer = QTimer()
            image_gallery_update_timer.singleShot(1000, self.handle_image_gallery_label)
            self.user_control_model.get_user().image_count += 1
            
            self.mediator.notify(sender = 'image_capture_presenter', receiver = 'template_image_preview_presenter', event = 'update_template_with_a_image', data = {'selected_image_id': self.user_control_model.get_user().image_count})
            
            self.view.update_number_of_captured_images_gui(self.user_control_model.get_user().image_count, 
                                                           self.template_control_model.get_template_with_field_from_database(self.template_control_model.selected_template_id, 'number_of_images'))    
        else:
            print("Out of images in template")
            
    def handle_update_preview_image(self) -> None:
        frame = self.model.get_frame()
        if frame is not None:       
            self.view.update_preview_image_gui(frame)
            
            
    def handle_update_number_of_captured_images(self, number_of_images: int = None, number_of_templates: int = None) -> None:
        if number_of_images is not None:
            self.view.update_number_of_captured_images_gui(number_of_images, number_of_templates)
        else:
            self.view.update_number_of_captured_images_gui(self.user_control_model.get_user().image_count, self.template_control_model.get_template_with_field_from_database(self.template_control_model.selected_template_id, 'number_of_images'))

    def handle_update_preview_fps(self) -> None:
        fps = self.model.get_fps()
        if fps is not None:
            self.view.update_preview_fps_gui(fps)
    
    
    def handle_start_update_preview_image(self) -> None:
        self.frame_update_timer.start(10)
        
    def handle_stop_update_preview_image(self) -> None:
        self.model.stop_preview_process()
        
        
    def handle_image_gallery_label(self):
        self.view.image_gallery_container_widget.setGeometry(0,
                                                             0,
                                                             self.user_control_model.get_user().image_count * 250 + 30,
                                                             200)

        self.view.image_gallery_frame.mousePressEvent = self.handle_mouse_press_event_small_image_label_in_menu_frame()
        self.view.image_gallery_frame.mouseMoveEvent = self.handle_mouse_move_event_small_image_label_in_menu_frame()
        # self.view.template_menu_frame.mouseReleaseEvent = self.handle_mouse_release_event_small_image_label_in_menu_frame()   
        # for i in range(0, self.user_control_model.get_user().image_count + 1):
        small_image_label = QLabel()
        small_image_label.setMinimumSize(250, 200)
        small_image_label.setMaximumSize(250, 200)
        image_pixmap = QPixmap (self.user_control_model.get_user().gallery_folder_path + f"/image{self.user_control_model.get_user().image_count - 1}.png")
        small_image_label.setPixmap(image_pixmap.scaled(250, 200, Qt.KeepAspectRatio))
        # small_image_label.mousePressEvent = self.handle_mouse_press_event_small_image_label_in_menu()  # Thiết lập sự kiện click
        small_image_label.mouseReleaseEvent = self.handle_mouse_release_event_small_image_label_in_menu(self.current_index)
        # small_image_label.mouseMoveEvent = self.handle_mouse_move_event_small_image_label_in_menu()
        self.view.image_gallery_container_layout.insertWidget(0,small_image_label)
        self.small_image_labels.append(small_image_label)
        self.current_index += 1
        
    def handle_clear_image_gallery_label(self):
        self.current_index = 1
        self.small_image_labels = []
        # Xóa tất cả các widget trong layout
        while self.view.image_gallery_container_layout.count():
            item = self.view.image_gallery_container_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            
    def handle_delete_image_in_gallery(self, index_of_image: int):
        self.user_control_model.get_user().image_count -= 1
        self.view.update_number_of_captured_images_gui(self.user_control_model.get_user().image_count, self.template_control_model.get_template_with_field_from_database(self.template_control_model.selected_template_id, 'number_of_images'))
        
        self.small_image_labels[index_of_image - 1].clear()
        # self.small_image_labels[index_of_image - 1].setStyleSheet("background-color: #0000ff;")
        
        
        # self.view.capture_button.setEnabled(True)
        self.deleted_image_indexes.append(index_of_image)
        
        
    def hanđle_restart_capture_and_save_and_update_image_gallery(self, index_of_image: int):
        print(self.user_control_model.get_user().gallery_folder_path)
        if self.user_control_model.get_user().image_count < self.template_control_model.get_template_with_field_from_database(self.template_control_model.selected_template_id,'number_of_images'):
            # self.model.capture_signal_queue.put(obj = self.user_control_model.get_user().gallery_folder_path)
            # self.model.image_captured_count.put(obj = self.user_control_model.get_user().image_count)
            # self.model.number_of_images.put(obj = self.template_control_model.get_template_with_field_from_database(self.template_control_model.selected_template_id, 'number_of_images'))
            self.model.capture_image(user_image_gallery_folder_path = self.user_control_model.get_user().gallery_folder_path,
                                     image_captured_count = self.user_control_model.get_user().image_count,
                                     index_of_image = index_of_image - 1)
            # print(self.image_control_model.database_path)
            self.image_control_model.update_image_in_database(id = index_of_image,
                                                              name = f"image{index_of_image - 1}.png",
                                                              path = self.user_control_model.get_user().gallery_folder_path + f"/image{index_of_image - 1}.png",
                                                              size = (2592,1944),
                                                             template_with_image_path=self.user_control_model.get_user().gallery_folder_path + f"/template_with_image{index_of_image - 1}.png"
                                                                )
            
            self.template_export_model.export_template_with_a_image(self.template_control_model.get_template_from_database(self.template_control_model.selected_template_id),
                                                                    self.image_control_model.get_image_from_database(index_of_image),
                                                                    None,
                                                                    None)
            
            self.mediator.notify(sender = 'image_capture_presenter', receiver = 'template_image_preview_presenter', event = 'update_template_with_a_image', data = {'selected_image_id': index_of_image})
            
            # image_gallery_update_timer = QTimer()
            # image_gallery_update_timer.singleShot(1000, self.handle_image_gallery_label)
            
            
            self.small_image_labels[index_of_image - 1].clear()
            image_pixmap = QPixmap(self.image_control_model.get_image_with_field_from_database(index_of_image, 'path'))
            self.small_image_labels[index_of_image - 1].setPixmap(QPixmap(image_pixmap.scaled(250, 200, Qt.KeepAspectRatio)))
            
            
            
            self.user_control_model.get_user().image_count += 1
            self.view.update_number_of_captured_images_gui(self.user_control_model.get_user().image_count, 
                                                           self.template_control_model.get_template_with_field_from_database(self.template_control_model.selected_template_id, 'number_of_images'))    
        else:
            print("Out of images in template")
    
    # overide mouse event method for small template in menu for template menu frame
    def handle_mouse_press_event_small_image_label_in_menu_frame(self):
        def handler(event):
            
            if event.button() == Qt.LeftButton:
                self.start_pos = event.pos()
        return handler
    
    def handle_mouse_move_event_small_image_label_in_menu_frame(self):
        def handler(event):
            if self.start_pos:
                # print(event.pos())
                delta = event.pos() - self.start_pos
                new_x = self.view.image_gallery_container_widget.x() + delta.x()
                # print(new_x)
                # print(self.view.image_gallery_container_widget.x())
                if self.view.image_gallery_container_widget.width() >= 1030:
                    new_x = max(min(new_x, 0), (1030 - self.view.image_gallery_container_widget.width())) # Ensure new_x is between -600 and 0
                else:
                    new_x = 0
                self.view.image_gallery_container_widget.move(new_x, self.view.image_gallery_container_widget.y())
                self.start_pos = event.pos()  
                if delta.x() > 5:
                    self.touch_event = "Swipe right"
                elif delta.x() < -5:
                    self.touch_event = "Swipe left"
            
        return handler
    
    def handle_mouse_release_event_small_image_label_in_menu_frame(self):
        def handler(event):
            pass
        return handler
    
    
    # overide mouse event method for small template in menu for template menu label
    def handle_mouse_press_event_small_image_label_in_menu(self):
        def handler(event):
            pass
            # if event.button() == Qt.LeftButton:
            #     self.start_pos = event.pos()
                
            
        return handler
    
    def handle_mouse_move_event_small_image_label_in_menu(self):
        def handler(event):
            pass
        return handler
    
    
    def handle_mouse_release_event_small_image_label_in_menu(self, index):
        
        def handler(event):
            if event.button() == Qt.LeftButton:
                if self.touch_event == "Touch":
                    print(index)
                    
                    # self.mediator.notify(sender = 'image_capture_presenter', receiver = 'template_image_preview_presenter', event = 'update_raw_image', data = {'selected_image_id': index})
                    if self.deleted_image_indexes.count(index) == 0:
                        
                        self.mediator.notify(sender = 'image_capture_presenter', receiver = 'template_image_preview_presenter', event = 'update_template_with_a_image', data = {'selected_image_id': index})
                        
                        self.stack_view.setCurrentIndex(4)
                    # for label in self.small_image_labels:
                    #     if label.geometry().contains(self.view.image_gallery_container_widget.mapFromParent(event.pos())):
                    #         self.view.update_template_show_label(self.template_control_model.get_template_with_field_from_database(index, 'path'))  # Kích thước lớn hơn
                    #         self.selected_template_id = index
                    #         break
                    # self.view.TMV_touch_event_signal.emit("Touch")
                elif self.touch_event == "Swipe right":
                    pass
                    # self.view.TMV_touch_event_signal.emit("Swipe right")
                elif self.touch_event == "Swipe left":
                    pass
                    # self.view.TMV_touch_event_signal.emit("Swipe left")
                print(self.touch_event)
            self.touch_event = "Touch"
        return handler