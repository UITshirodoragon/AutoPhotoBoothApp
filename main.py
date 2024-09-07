from View.Image_Capture_View import ImageCaptureView

from Presenter.Image_Capture_Presenter import ImageCapturePresenter
from Model.Image_Processing_Model import ImageProcessingModel
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Tạo view và presenter
    view = ImageCaptureView()
    model = ImageProcessingModel()
    presenter = ImageCapturePresenter(view, model)

    # Hiển thị giao diện
    view.show()

    # Xử lý khi đóng cửa sổ
    def close_app():
        presenter.handle_stop_update_image()
        app.quit()

    view.closeEvent = lambda event: close_app()

    sys.exit(app.exec_())
