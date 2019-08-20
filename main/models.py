from django.db import models

# Create your models here.

class Planet(models.Model):
    name = models.CharField(default='', max_length=32, verbose_name='Название планеты', unique=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Планета'
        verbose_name_plural = 'Планеты'

class Sith(models.Model):
    name = models.CharField(default='', max_length=32, verbose_name='Имя ситха', unique=True)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, verbose_name='Планета')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ситх'
        verbose_name_plural = 'Ситхи'

class Recruit(models.Model):
    name = models.CharField(default='', max_length=32, verbose_name='Имя')
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, verbose_name='Планета')
    age = models.IntegerField(default=18, verbose_name='Возраст')
    email = models.CharField(default='', max_length=256, verbose_name='Email')
    master = models.ForeignKey(Sith, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рекрут'
        verbose_name_plural = 'Рекруты'

class Questions(models.Model):
    text = models.CharField(default='', max_length=256, verbose_name='Вопрос')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Replys(models.Model):
    recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE, blank=True, null=True)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, blank=True, null=True)
    answer = models.BooleanField(default=0)

