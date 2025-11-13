from abc import ABC, abstractmethod

# Abstract Product
class Notification(ABC):
    @abstractmethod
    def send(self):
        pass


# Concrete Products
class EmailNotification(Notification):
    def send(self):
        print("Sending Email notification.")


class SMSNotification(Notification):
    def send(self):
        print("Sending SMS notification.")


# Abstract Creator
class NotificationCreator(ABC):
    @abstractmethod
    def create_notification(self):
        pass


# Concrete Creators
class EmailNotificationCreator(NotificationCreator):
    def create_notification(self):
        return EmailNotification()


class SMSNotificationCreator(NotificationCreator):
    def create_notification(self):
        return SMSNotification()


# Client Code
if __name__ == "__main__":
    email_notif = EmailNotificationCreator().create_notification()
    sms_notif = SMSNotificationCreator().create_notification()

    email_notif.send()
    sms_notif.send()
