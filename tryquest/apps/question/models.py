from django.db import models

from tryquest.apps.admin.models import Admin, AdminGroup


# TODO implement validation for Question - Correct answer count

class Question(models.Model):
    class QuestionTypes:
        SINGLE_ANSWER = 1
        MULTI_ANSWER = 2
        TRUE_FALSE = 3
        ONE_WORD = 4

        CHOICES = (
            ("Single Answer", SINGLE_ANSWER),
            ("Multiple Answer", MULTI_ANSWER),
            ("True or False", TRUE_FALSE),
            ("One Word", ONE_WORD)
        )

    author = models.ForeignKey(Admin)
    admin_group = models.ForeignKey(AdminGroup, null=True)

    text = models.TextField()
    date_added = models.DateTimeField()
    type = models.IntegerField(choices=QuestionTypes.CHOICES)
    tags = models.ManyToManyField("Tag")
    points = models.IntegerField(default=1)


class Tag(models.Model):
    name = models.CharField(max_length=100, choices="abcdefghijklmnopqrstuvwxyz-")


class Option(models.Model):
    question = models.ForeignKey(Question)
    name = models.TextField()
    is_correct = models.BooleanField()


class TrueFalseOption(models.Model):
    question = models.ForeignKey(Question)
    answer = models.BooleanField()


class OneWordAnswer(models.Model):
    question = models.ForeignKey(Question)
    answer = models.CharField(max_length=255)
