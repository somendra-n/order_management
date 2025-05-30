from django.db import models

class Order(models.Model):
    """
    The Order model represents a single order in the system.
    It contains a title and a description, which can be used
    to store key details about the order.
    """

    # Short title of the order (max length 255 characters)
    title = models.CharField(max_length=255)

    # Detailed description of what the order contains or represents
    description = models.TextField()

    def __str__(self):
        """
        Returns a human-readable string representation of the order,
        useful in the admin panel and Django shell.
        """
        return self.title
