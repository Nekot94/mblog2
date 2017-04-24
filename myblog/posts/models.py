from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField("Заголовок", max_length=120)
	content = models.TextField("Содержимое")
	timestamp = models.DateTimeField("Создана", auto_now=False, auto_now_add=True)
	updated = models.DateTimeField("Обновлена", auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Статья"
		verbose_name_plural = "Статьи"
