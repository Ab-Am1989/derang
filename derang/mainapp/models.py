from django.db import models
import datetime
# from django.contrib.gis.db import models
from location_field.models.plain import PlainLocationField


def year_choices():
    return [(r, r) for r in range(1984, datetime.date.today().year + 1)]


def current_year():
    return datetime.date.today().year


# Create your models here.
class Movie(models.Model):
    class Meta:
        verbose_name = \
            'فیلم'
        verbose_name_plural = 'فیلم'

    name = models.CharField('نام فیلم', max_length=150)
    director = models.CharField('نام کارگردان', max_length=100)
    year_choices = year_choices()
    year = models.IntegerField('سال تولید', choices=year_choices, default=current_year)

    COMEDIC_GENRE = 1
    DRAMA_GENRE = 2
    MUSICAL_GENRE = 3
    THRILLER_GENRE = 4
    ACTION_GENRE = 5
    ROMANCE_GENRE = 6
    MELODRAMA_GENRE = 7
    MYSTERY_GENRE = 8
    SCI_FI_GENRE = 9
    FANTASY_GENRE = 10
    HORROR_GENRE = 11
    WESTERN = 12
    NOIR_GENRE = 13
    ADVENTURE_GENRE = 14
    OTHERS = 15

    genre_choices = [
        (COMEDIC_GENRE, 'کمدی'),
        (DRAMA_GENRE, 'درام'),
        (MUSICAL_GENRE, 'موزیکال'),
        (THRILLER_GENRE, 'تریلر'),
        (ACTION_GENRE, 'اکشن'),
        (ROMANCE_GENRE, 'رمانتیک'),
        (MELODRAMA_GENRE, 'ملودرام'),
        (MYSTERY_GENRE, 'معمایی'),
        (SCI_FI_GENRE, 'علمی-تخیلی'),
        (FANTASY_GENRE, 'فانتزی'),
        (HORROR_GENRE, 'ترسناک'),
        (WESTERN, 'وسترن'),
        (NOIR_GENRE, 'نوآر'),
        (ADVENTURE_GENRE, 'ماجراجویانه'),
        (OTHERS, 'سایر'),
    ]

    genre = models.IntegerField('سبک', choices=genre_choices)

    def __str__(self):
        return self.name


class Book(models.Model):
    class Meta:
        verbose_name = \
            'کتاب'
        verbose_name_plural = 'کتاب'

    name = models.CharField('نام کتاب', max_length=150)
    author = models.CharField('نویسنده', max_length=150)
    publisher = models.CharField('انتشارات', max_length=100)

    LITERATURE = 1
    MYTHICAL = 2
    ECONOMY = 3
    ARCHEOLOGY = 4
    HISTORY = 5
    DAIRY = 6
    NOVEL = 7
    SHORT_STORY = 8
    MYSTICISM = 9
    RELIGION = 10
    PSYCHOLOGY = 11
    BIOGRAPHY = 12
    POLITICS = 13
    SOCIOLOGY = 14
    HUMANITIES = 15
    MEDICAL = 16
    PHILOSOPHY = 17
    CHILDREN_AND_TEENAGER = 18
    REPORTING = 19
    INTERVIEW = 20
    ARTICLE = 21
    MUSIC = 22
    ART = 23
    OTHERS = 24

    subject_choices = [
        (LITERATURE, 'ادبیات'),
        (MYTHICAL, 'اسطوره‌ای'),
        (ECONOMY, 'اقتصاد'),
        (ARCHEOLOGY, 'باستان‌شناسی'),
        (HISTORY, 'تاریخ'),
        (DAIRY, 'خاطره‌نویسی'),
        (NOVEL, 'رمان'),
        (SHORT_STORY, 'داستان کوتاه'),
        (MYSTICISM, 'عرفان'),
        (RELIGION, 'دین'),
        (PSYCHOLOGY, 'روان‌شناسی'),
        (SOCIOLOGY, 'جامعه‌نویسی'),
        (HUMANITIES, 'علوم‌انسانی'),
        (MEDICAL, 'پزشکی'),
        (PHILOSOPHY, 'فلسفه'),
        (CHILDREN_AND_TEENAGER, 'کودک و نوجوان'),
        (REPORTING, 'گزارش‌نویسی'),
        (INTERVIEW, 'مصاحبه'),
        (ARTICLE, 'مقاله'),
        (MUSIC, 'موسیقی'),
        (ART, 'هنر'),
        (OTHERS, 'سایر'),
    ]
    subject = models.IntegerField('موضوع', choices=subject_choices)

    def __str__(self):
        return self.name


class Song(models.Model):
    class Meta:
        verbose_name = \
            'ترانه'
        verbose_name = 'ترانه'

    name = models.CharField('نام اثر', max_length=200)
    singer = models.CharField('خواننده', max_length=150)
    composer = models.CharField('آهنگساز', max_length=150)
    songwriter = models.CharField('ترانه‌سرا', max_length=150)

    # language: add this field later

    def __str__(self):
        return self.name


class Theater(models.Model):
    class Meta:
        verbose_name = 'تئاتر'
        verbose_name_plural = 'تئاتر'

    name = models.CharField('نام اثر', max_length=200)
    director = models.CharField('کارگردان', max_length=150)
    scriptwriter = models.CharField('نمایشنامه‌نویس', max_length=150)
    genre_choices = Movie.genre_choices
    genre = models.IntegerField('ژانر', choices=genre_choices)

    def __str__(self):
        return self.name


class Journey(models.Model):
    class Meta:
        verbose_name = 'سفر'
        verbose_name_plural = 'سفر'

    title = models.CharField('عنوان', max_length=255)
    city = models.CharField('شهر', max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    country = models.CharField('کشور', max_length=100)
    province = models.CharField('استان/ایالت', max_length=100)

    def __str__(self):
        return self.title
