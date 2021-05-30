from django.db import models


KEYS =(
    ("1", "1-0"),
    ("2", "0-1"),
    ("3", "0-2-3"),
    ("4", "3-2-0"),
)


class Question(models.Model):
	ask = models.CharField('Вопрос', max_length=30)
	key_type = models.CharField(
		max_length=1,
		choices=KEYS)

	def __str__(self):
		return self.ask[:12]


class Answer(models.Model):
	first_name = models.CharField('Имя сдавшего', max_length=50)
	middle_name = models.CharField('Отчество', max_length=50, blank=True)
	last_name = models.CharField('Фамилия сдавшего', max_length=50)
	pub_date = models.DateTimeField('Дата ответа', auto_now_add=True)
	result = models.IntegerField('Сумма баллов', blank=True, null=True)
	email = models.EmailField('Почта', blank=True)