from django.db import models

# Create your models here.
class QuestionBankCSV(models.Model):
    Question_Detail = models.TextField(max_length=99999)
    Question_Image = models.TextField(max_length=99999, default=None, null=True)
    ID_Subject = models.IntegerField()
    Question_AnswerA = models.TextField(max_length=99999)
    Question_AnswerB = models.TextField(max_length=99999)
    Question_AnswerC = models.TextField(max_length=99999)
    Question_AnswerD = models.TextField(max_length=99999)
    Correct_Answer = models.TextField(max_length=99999)
    stt=models.IntegerField(default=None)
    class Meta:
        db_table='question_bank_csv'
    def __str__(self):
        return self.Question_Detail