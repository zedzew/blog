
from django.db import models
from random import randrange

class Migration(DataMigration):
    def forwards(self, orm):
        comments = orm.Comments.objects.all()
        for comment in comments:
            rand_id = randrange(1, 4)
            comment.comments_from = orm['auth.User'].objects.get(id=rand_id)
            comment.save()

    def backwards(self, orm):
        pass

    comments_from = models.ForeignKey(User)
    comments_data = models.DateTimeField()

from django.contrib.auth.models import User
default=datetime, date, today