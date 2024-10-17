from typing import Protocol


class IMediator(Protocol):
    def notify(self, sender: str, receiver: str, event: str, data: dict = None) -> None:
        ...
    
class ImageCapturePresenter(Protocol):
    def set_mediator(self, mediator: IMediator) -> None:
        ...

class TemplateMenuPresenter(Protocol):
    def set_mediator(self, mediator: IMediator) -> None:
        ...
        
class TemplateExportPresenter(Protocol):
    def set_mediator(self, mediator: IMediator) -> None:
        ...
        
    def handle_update_final_template_with_images(self) -> None:
        ...


class ConcreteMediator(IMediator):
    def __init__(self, 
                 image_capture_presenter: ImageCapturePresenter, 
                 template_menu_presenter: TemplateMenuPresenter, 
                 template_export_presenter: TemplateExportPresenter) -> None:
        self.image_capture_presenter: ImageCapturePresenter = image_capture_presenter
        self.template_menu_presenter: TemplateMenuPresenter = template_menu_presenter
        self.template_export_presenter: TemplateExportPresenter = template_export_presenter

        self.image_capture_presenter.set_mediator(self)
        self.template_menu_presenter.set_mediator(self)
        self.template_export_presenter.set_mediator(self)

    def notify(self, sender: str, receiver: str, event: str, data: dict = None) -> None:
        if sender == 'image_capture_presenter' and receiver == 'template_menu_presenter':
            if event == 'update_final_template_with_images':
                self.template_export_presenter.handle_update_final_template_with_images()