from django.db import models


class Poll(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class Question(models.Model):
    QUESTION_TYPE_CHOICES = (
        ('TEXT', 'Text'),
        ('RADIOBUTTON', 'RadioButton'),
        ('CHECKBOX', 'CheckBox'),
    )

    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=300)
    question_type = models.CharField(max_length=20,
                                     choices=QUESTION_TYPE_CHOICES)
    poll_id = models.ForeignKey(Poll, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class QuestionChoice(models.Model):
    id = models.AutoField(primary_key=True)
    choice = models.CharField(max_length=100)
    question_id = models.ForeignKey(Question,
                                    on_delete=models.CASCADE)

    def __str__(self):
        return self.choice


class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    answer = models.CharField(max_length=200)
    question_id = models.ForeignKey(Question,
                                    on_delete=models.CASCADE)

    class Meta:
        unique_together = [['user_id', 'question_id']]

    def __str__(self):
        return self.answer
