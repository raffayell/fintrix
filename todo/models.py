from django.db import models

class Project(models.Model):
    name = models.CharField("Project", max_length=50, unique=True)

    def __str__(self):
        return self.name


class Todo(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(null=True, blank=True)
    urgent = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    related_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title[:10]} - {self.related_project}"