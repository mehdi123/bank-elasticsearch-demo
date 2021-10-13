from django.db import models
from haystack import signals

from customers.models import Customer

class UserOnlySignalProcessor(signals.BaseSignalProcessor):
    def setup(self):
        models.signals.post_save.connect(self.handle_save, sender=Customer)
        models.signals.post_delete.connect(self.handle_delete, sender=Customer)

    def teardown(self):
        models.signals.post_save.disconnect(self.handle_save, sender=Customer)
        models.signals.post_delete.disconnect(self.handle_delete, sender=Customer)