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

from PyQt5.QtWidgets import QApplication, QStackedWidget, QScrollArea, QMainWindow, QWidget, QVBoxLayout, QScrollArea
from PyQt5.QtCore import QSize, QRect, Qt
from PyQt5.QtGui import QScreen
import sys

import platform as plf


def handle_app_show_on_portrait_screen(screen: QScreen, stack_view: QStackedWidget):
    # Đặt cửa sổ vào màn hình phụ
    stack_view.move(screen.geometry().topLeft())
    
    # Chuyển sang chế độ toàn màn hình
    return stack_view
    
def handle_app_show_on_landscape_screen(screen, stack_view: QStackedWidget):
    main_widget = QWidget()
    main_widget.resize(540, 960)
    main_widget.setMaximumSize(QSize(1938, 1938))
    main_layout = QVBoxLayout(main_widget)
    main_layout.setObjectName(u"main_layout")
    main_layout.setAlignment(Qt.AlignCenter)
    main_scroll_area = QScrollArea(main_widget)
    main_scroll_area.setMaximumSize(QSize(1100, 2000))
    main_scroll_area.setObjectName(u"scrollArea")
    main_scroll_area.setMinimumSize(QSize(540, 960))
    main_scroll_area.setLineWidth(2)
    # scrollArea.setFrameShape(QScrollArea.NoFrame)
    # scrollArea.setFrameShadow(QScrollArea.Plain)
    main_scroll_area.setWidgetResizable(True)
    scroll_area_content_container_widget = QWidget()
    scroll_area_content_container_widget.setObjectName(u"scroll_area_content_container_widget")
    scroll_area_content_container_widget.setGeometry(QRect(0, 0, 1080, 1920))
    scroll_area_content_container_widget_layout = QVBoxLayout(scroll_area_content_container_widget)
    scroll_area_content_container_widget_layout.setObjectName(u"scroll_area_content_container_widget_layout")
    stack_view.setParent(scroll_area_content_container_widget)
    stack_view.setObjectName(u"stack_view")
    stack_view.setMinimumSize(QSize(1080, 1920))
    
    scroll_area_content_container_widget_layout.addWidget(stack_view)

    main_scroll_area.setWidget(scroll_area_content_container_widget)

    main_layout.addWidget(main_scroll_area)
    
    
    # Đặt cửa sổ vào màn hình phụ
    main_widget.move(screen.geometry().topLeft())
    
    return main_widget
    # main_widget.show()

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
    
    # stack_view.show()
    
    # Lấy danh sách các màn hình
    screens = app.screens()
    main_screen = screens[0]
    # Giả sử màn hình phụ là màn hình thứ hai (index 1)
    if(plf.system() == "Windows"):
        if len(screens) > 1:
            secondary_screen = screens[1]
            main_widget = handle_app_show_on_portrait_screen(secondary_screen, stack_view)
            main_widget.showFullScreen()
        else:
            print("Không tìm thấy màn hình phụ.")
            main_widget = handle_app_show_on_landscape_screen(main_screen, stack_view)
            main_widget.showFullScreen()
    elif plf.system() == "Linux":
        
        main_widget = handle_app_show_on_portrait_screen(main_screen, stack_view)
        main_widget.showFullScreen()
    sys.exit(app.exec_())


