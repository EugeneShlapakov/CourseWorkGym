from django.db import models


class Coach(models.Model):
    name = models.CharField("Тренер:", max_length=150)
    specialization = models.TextField("Специализация")
    url = models.SlugField(max_length=160, unique=True)
    image = models.ImageField("Фото", upload_to="coaches/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Наши тренеры"
        verbose_name_plural = "Наши тренеры"


class Gym(models.Model):
    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="gyms/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Наши залы"
        verbose_name_plural = "Наши залы"


class Service(models.Model):
    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="services/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Наши услуги"
        verbose_name_plural = "Наши услуги"


class Pricing(models.Model):
    name = models.CharField("Название", max_length=100)
    price = models.PositiveIntegerField("Цена")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Цены"
        verbose_name_plural = "Цены"


class Gallery(models.Model):
    name = models.CharField("Название", max_length=100)
    image = models.ImageField("Изображение", upload_to="gallery/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Галлерея"
        verbose_name_plural = "Галлерея"
