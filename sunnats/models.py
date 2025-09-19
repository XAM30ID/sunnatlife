import os

from django.db import models


def sunnat_category_path(instance, filename):
    return os.path.join('images/sunnats_categories', f'{instance.slug}.{filename.split('.')[-1]}')

class SunnatCategory(models.Model):
    '''
        Класс для категорий сунн.
    '''
    title = models.CharField(verbose_name='Название категории', max_length=128)
    slug = models.SlugField(verbose_name='Слаг категории')
    image = models.FileField(verbose_name='Изображение категории', upload_to=sunnat_category_path)

    def get_sunnats_count(self):
        return Sunnat.objects.filter(category__slug=self.slug).count()

    def get_sunnats(self):
        return Sunnat.objects.filter(category__slug=self.slug)

    def __str__(self):
        return f'Категория {self.title}'
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def delete(self):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        return super().delete()

    def save(self):
        if self.pk:
            old_instance = SunnatCategory.objects.get(pk=self.pk)
            if old_instance.image and old_instance.image != self.image:
                os.remove(old_instance.image.path)
        return super().save()



def person_path(instance, filename):
    return os.path.join('images/persons', f'{instance.slug}.{filename.split('.')[-1]}')

class Person(models.Model):
    '''
        Класс для описания личностей и биографий.
    '''
    PERSON_TYPES = [
        ('prophet', 'Пророк'),
        ('companion', 'Сподвижник'),
        ('other', 'Другое'),
    ]
    name = models.CharField(verbose_name='Имя', max_length=255)
    slug = models.SlugField(verbose_name='Слаг')
    figure_type = models.CharField(
        verbose_name="Тип личности", max_length=20,  choices=PERSON_TYPES, default='other')
    name_ar = models.CharField(verbose_name='Имя на арабском', max_length=255)
    birth_year = models.CharField(verbose_name='Год рождения', blank=True, null=True)
    death_year = models.CharField(verbose_name='Год смерти', blank=True, null=True)
    biography = models.TextField(verbose_name='Биография')
    caligraphy = models.FileField(verbose_name='Калиграфия', blank=True, null=True, upload_to=person_path)

    def get_name_with_respect(self):
        if self.figure_type == 'prophet':
            return {
                'ru': f"{self.name} (мир ему и благословение Аллаха)",
                'ar': f"{self.name_ar} (صلى الله عليه و سلم)"
                }
        elif self.figure_type == 'companion':
            return {
                'ru': f"{self.name} (да будет доволен им Аллах)",
                'ar': f"{self.name_ar} (رضي الله عنه)"
                }
        # elif self.figure_type in ['scholar', 'righteous']:
        #     return f"{self.name_ru} (да помилует его Аллах)"
        return {
            'ru': self.name,
            'ar': self.name_ar
            }

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'
    
    def delete(self):
        if self.caligraphy:
            if os.path.isfile(self.caligraphy.path):
                os.remove(self.caligraphy.path)
        return super().delete()

    def save(self):
        if self.pk:
            old_instance = Person.objects.get(pk=self.pk)
            if old_instance.caligraphy and old_instance.caligraphy != self.caligraphy:
                os.remove(old_instance.caligraphy.path)
        return super().save()


def sunnat_path(instance, filename):
    return os.path.join('images/sunnats', f'{instance.slug}.{filename.split('.')[-1]}')

class Sunnat(models.Model):
    '''
        Класс для сунн.
    '''
    title = models.CharField(verbose_name='Название сунны', max_length=255)
    slug = models.SlugField(verbose_name='Слаг сунны')
    category = models.ForeignKey(verbose_name='Категория', to=SunnatCategory, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст сунны', null=True, blank=True)
    image = models.FileField(verbose_name='Изображение для сунны', upload_to=sunnat_path, null=True, blank=True)
    
    def get_hadithes(self):
        return SunnatHadith.objects.filter(sunnat__slug=self.slug)

    def __str__(self):
        return f'Сунна {self.title}'
    
    class Meta:
        verbose_name = 'Сунна'
        verbose_name_plural = 'Сунны'

    def delete(self):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        return super().delete()

    def save(self):
        if self.pk:
            old_instance = Sunnat.objects.get(pk=self.pk)
            if old_instance.image and old_instance.image != self.image:
                os.remove(old_instance.image.path)
        return super().save()
    


class SunnatHadith(models.Model):
    '''
        Класс для хадисов от передатчиков.
    '''
    sender = models.ForeignKey(verbose_name='Передатчик', to=Person, on_delete=models.SET_DEFAULT, default='Неизвестно')
    sunnat = models.ForeignKey(verbose_name='Сунна', to=Sunnat, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст сунны')
    text_ar = models.TextField(verbose_name='Текст сунны на арабском')
    
    def __str__(self):
        return f'Хадис от {self.sender}'
    
    class Meta:
        verbose_name = 'Хадис'
        verbose_name_plural = 'Хадисы'
