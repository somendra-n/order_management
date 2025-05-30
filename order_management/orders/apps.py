
from django.apps import AppConfig

class OrdersConfig(AppConfig):
    """
    Configuration class for the 'orders' app.
    This sets default settings and behaviors when the app is loaded.
    """
    
    # Use BigAutoField by default for primary keys (useful for large datasets)
    default_auto_field = 'django.db.models.BigAutoField'

    # Register this app under the name 'orders'
    name = 'orders'
