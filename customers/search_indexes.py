from .models import Customer
from haystack import indexes
 
 
class CustomerIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    first_name = indexes.CharField(model_attr='first_name')
    last_name = indexes.CharField(model_attr='last_name')
    other_names = indexes.CharField(model_attr='other_names')
    email = indexes.CharField(model_attr='email', default=" ")
    phone = indexes.CharField(model_attr='phone', default=" ")
    balance = indexes.IntegerField(model_attr='balance', default="0")
    customer_status = indexes.CharField(model_attr='customer_status')
    address = indexes.CharField(model_attr='address', default=" ")

    content_auto = indexes.EdgeNgramField(model_attr='first_name')
 
    def get_model(self):
        return Customer
 
    def index_queryset(self, using=None):
        if using == 'default':
            return self.get_model().objects.all()
        return self.get_model().objects.none()
