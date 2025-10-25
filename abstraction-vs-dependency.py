from abc import ABC, abstractmethod


class NotificationService(ABC):
    @abstractmethod
    def notify(self, message: str):
        """Send a notification with the given message."""
        pass


class EmailNotification(NotificationService):
    def notify(self, message: str):
        print(f"Email sent: {message}")


class BookingService:
    def __init__(self, notification_service: NotificationService):
        """
        Initialize the booking service with a notification service.
        
        Args:
            notification_service (NotificationService): Any service implementing NotificationService.
        """
        self.notification_service = notification_service

    def process_booking(self, message: str):
        """Process a booking and notify the user."""
        self.notification_service.notify(message)


def main():
    email_notification = EmailNotification()
    booking_service = BookingService(email_notification)
    booking_service.process_booking("Your booking is confirmed!")


if __name__ == "__main__":
    main()
