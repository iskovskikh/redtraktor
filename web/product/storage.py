from django.core.files.storage import FileSystemStorage
from django.conf import settings

class MyImageStorage(FileSystemStorage):
    def save(self, name, content, max_length=None):
        if name is None:
            name = content.name

        if self.exists(name):
            return name
        else:
            super(MyImageStorage,self).save(name, content, max_length)