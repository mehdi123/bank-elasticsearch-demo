from .models import MultiModel
from haystack import indexes
 
 
class MultiModelIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    content = indexes.CharField(model_attr='content', default='')
    content_fr = indexes.CharField(model_attr='content_fr', default='')
    content_de = indexes.CharField(model_attr='content_de', default='')

    language = indexes.CharField(model_attr='language', default='default')

    #content_auto = indexes.EdgeNgramField(model_attr='content_de')

    def get_model(self):
        return MultiModel
 
    def index_queryset(self, using=None):
        return self.get_model().objects.filter(language=using).all()
