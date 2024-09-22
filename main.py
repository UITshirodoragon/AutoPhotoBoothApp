from View.Image_Capture_View import ImageCaptureView
from View.Start_View import *
from View.Template_Menu_View import TemplateMenuView
from View.Template_Export_View import TemplateExportView

from Presenter.Image_Capture_Presenter import ImageCapturePresenter
from Presenter.Start_Presenter import *
from Presenter.Template_Menu_Presenter import TemplateMenuPresenter
from Presenter.Template_Export_Presenter import TemplateExportPresenter

from Model.Image_Processing_Model import ImageProcessingModel
from Model.Start_Model import *
from Model.Template_Menu_Model import TemplateMenuModel
from Model.Template_Export_Model import TemplateExportModel

from PyQt5.QtWidgets import QApplication, QStackedWidget
import sys


if __name__ == "__main__":

    app = QApplication(sys.argv)
    
    stack_view = QStackedWidget()
    
    start_model = StartModel()
    start_view = StartView()
    start_presenter = StartPresenter(start_model, start_view, stack_view)

    template_menu_model = TemplateMenuModel()
    template_menu_view = TemplateMenuView()
    template_menu_presenter = TemplateMenuPresenter(template_menu_model, template_menu_view, stack_view)
    
    image_capture_view = ImageCaptureView()
    image_capture_model = ImageProcessingModel()
    image_capture_presenter = ImageCapturePresenter(image_capture_model,image_capture_view, stack_view)
    
    template_export_model = TemplateExportModel()
    template_export_view = TemplateExportView()
    template_export_presenter = TemplateExportPresenter(template_export_model, template_export_view, stack_view)
    
    
    stack_view.addWidget(start_view)
    stack_view.addWidget(template_menu_view)
    stack_view.addWidget(image_capture_view)
    stack_view.addWidget(template_export_view)
    
    
    stack_view.setCurrentIndex(0)
    
    stack_view.show()

    
    
    # # Tạo view và presenter
    # view = ImageCaptureView()
    # model = ImageProcessingModel()
    # presenter = ImageCapturePresenter(view, model)

    # # Hiển thị giao diện
    # view.show()

    # Xử lý khi đóng cửa sổ
    # def close_app():
    #     presenter.handle_stop_update_image()
    #     app.quit()

    # view.closeEvent = lambda event: close_app()

    sys.exit(app.exec_())
