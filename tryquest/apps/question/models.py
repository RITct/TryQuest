from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


# TODO implement validation for Question - Correct answer count

class Question(models.Model):
    # TODO Future Feature
    # class QuestionTypes:
    #     SINGLE_ANSWER = 1
    #     MULTI_ANSWER = 2
    #     TRUE_FALSE = 3
    #     ONE_WORD = 4
    #
    #     CHOICES = (
    #         ("Single Answer", SINGLE_ANSWER),
    #         ("Multiple Answer", MULTI_ANSWER),
    #         ("True or False", TRUE_FALSE),
    #         ("One Word", ONE_WORD)
    #     )

    author = models.ForeignKey(User)

    text = models.TextField()
    date_added = models.DateTimeField()
    # type = models.IntegerField(choices=QuestionTypes.CHOICES, default=QuestionTypes.SINGLE_ANSWER)
    tags = models.ManyToManyField("Tag")
    points = models.IntegerField(default=1)


class Tag(models.Model):
    TagValidator = RegexValidator(regex="[a-bA-B_]+")
    name = models.CharField(max_length=100, validators=[TagValidator])


class Option(models.Model):
    question = models.ForeignKey(Question)
    name = models.TextField()
    is_correct = models.BooleanField()

# TODO Future Feature
# class TrueFalseOption(models.Model):
#     question = models.ForeignKey(Question)
#     answer = models.BooleanField()
#
#
# class OneWordAnswer(models.Model):
#     question = models.ForeignKey(Question)
#     answer = models.CharField(max_length=255)
