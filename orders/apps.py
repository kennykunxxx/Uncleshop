from django.apps import AppConfig


class OrdersConfig(AppConfig):
    name = 'orders'
    
    def ready(self):
        # signals are imported, so that they are defined and can be used
        import orders.signals
