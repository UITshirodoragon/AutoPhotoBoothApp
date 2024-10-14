class PresenterBusDriver:
    def __init__(self):
        self.presenters = {}

    def register_presenter(self, name, presenter):
        self.presenters[name] = presenter

    def send_message(self, sender_name, receiver_name, message):
        if receiver_name in self.presenters:
            receiver = self.presenters[receiver_name]
            receiver.receive_message(sender_name, message)
        else:
            print(f"Presenter {receiver_name} not found")

    def broadcast_message(self, sender_name, message):
        for name, presenter in self.presenters.items():
            if name != sender_name:
                presenter.receive_message(sender_name, message)

class Presenter:
    def receive_message(self, sender_name, message):
        print(f"Received message from {sender_name}: {message}")

# Example usage
if __name__ == "__main__":
    bus_driver = PresenterBusDriver()
    
    presenter_a = Presenter()
    presenter_b = Presenter()
    
    bus_driver.register_presenter("PresenterA", presenter_a)
    bus_driver.register_presenter("PresenterB", presenter_b)
    
    bus_driver.send_message("PresenterA", "PresenterB", "Hello from A")
    bus_driver.broadcast_message("PresenterA", "Hello everyone from A")