from View.Image_Capture_View import ImageCaptureView
from View.Start_View import StartView
from View.Template_Menu_View import TemplateMenuView
from View.Template_Export_View import TemplateExportView

from Presenter.Start_Presenter import StartPresenter
from Presenter.Image_Capture_Presenter import ImageCapturePresenter
from Presenter.Template_Menu_Presenter import TemplateMenuPresenter
from Presenter.Template_Export_Presenter import TemplateExportPresenter
from Presenter.Mediator import IMediator, ConcreteMediator


from Model.Image_Capture_Model import ImageCaptureModel
from Model.Start_Model import StartModel
from Model.Template_Menu_Model import TemplateMenuModel
from Model.Template_Export_Model import TemplateExportModel
from Model.User_Model import UserModel, User
from Model.Template_Model import TemplateModel 

from PyQt5.QtWidgets import QApplication, QStackedWidget, QScrollArea, QMainWindow
import sys

import platform as plf

if __name__ == "__main__":

    app = QApplication(sys.argv)
    
    stack_view = QStackedWidget()
    
    user_control_model = UserModel()
    template_control_model = TemplateModel()
    start_model = StartModel()
    template_menu_model = TemplateMenuModel()
    image_capture_model = ImageCaptureModel()
    template_export_model = TemplateExportModel()
    
    start_view = StartView()
    template_menu_view = TemplateMenuView()
    image_capture_view = ImageCaptureView()
    template_export_view = TemplateExportView()   
     
    start_presenter = StartPresenter(start_model, start_view, stack_view, user_control_model, app)

    template_menu_presenter = TemplateMenuPresenter(template_menu_model, template_menu_view, stack_view, user_control_model, template_control_model)
    
    template_export_presenter = TemplateExportPresenter(template_export_model, template_export_view, stack_view, user_control_model, template_control_model)
    
    image_capture_presenter = ImageCapturePresenter(image_capture_model,image_capture_view, stack_view, user_control_model, template_control_model)
    
    mediator = ConcreteMediator(image_capture_presenter, template_menu_presenter, template_export_presenter)
    
    stack_view.addWidget(start_view)
    stack_view.addWidget(template_menu_view)
    stack_view.addWidget(image_capture_view)
    stack_view.addWidget(template_export_view)
    
    
    stack_view.setCurrentIndex(0)
    
    stack_view.show()
    
    # Lấy danh sách các màn hình
    screens = app.screens()

    # Giả sử màn hình phụ là màn hình thứ hai (index 1)
    if(plf.system() == "Windows"):
        if len(screens) > 1:
            secondary_screen = screens[1]
            
            # Đặt cửa sổ vào màn hình phụ
            stack_view.move(secondary_screen.geometry().topLeft())
            
            # Chuyển sang chế độ toàn màn hình
            stack_view.showFullScreen()
        else:
            print("Không tìm thấy màn hình phụ.")
            
            # scroll_area = QScrollArea()
            # scroll_area.setWidget(stack_view)
            # scroll_area.setWidgetResizable(True)
            # main_window = QMainWindow()
            # main_window.setCentralWidget(scroll_area)
            
            # main_window.showFullScreen()
    


    sys.exit(app.exec_())
