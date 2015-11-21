from django.db import models
from django.contrib.auth.models import User, Group
from django.template.defaultfilters import slugify

# Create your models here.



class Forum(models.Model):
    name = models.CharField("Forum name", max_length=60)
    description = models.TextField("Description")
    viewable_by = models.ForeignKey(Group)
    super_admin = models.ForeignKey(User, related_name="super_admin")
    admins = models.ManyToManyField(User)
    dropdown_open = models.BooleanField("Subforums dropdown open by default", default=False)
    parent = models.ForeignKey("Forum", blank=True, null=True)
    slug = models.SlugField(max_length=20)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Forum, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Thread(models.Model):
    topic = models.CharField("Thread topic", max_length=60)
    started_by = models.ForeignKey(User)
    forum = models.ForeignKey(Forum)
    started_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=20)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.topic)
        super(Thread, self).save(*args, **kwargs)

    def __str__(self):
        return self.topic


class Post(models.Model):
    written_by = models.ForeignKey(User)
    thread = models.ForeignKey(Thread)
    content = models.TextField("Message")
    written_on = models.DateTimeField(auto_now_add=True)
    # slug = models.SlugField(max_length=20) things not really needed anymore
    reply_to = models.ForeignKey("Post", blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.content)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        to_return = str(self.thread.topic) + ' : ' + str(self.content)
        return to_return
