# Generated by Django 4.0.6 on 2022-08-17 07:27

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminDetail',
            fields=[
                ('MSQT', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(default=None, max_length=50)),
            ],
            options={
                'db_table': 'ad_information',
            },
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'exam',
            },
        ),
        migrations.CreateModel(
            name='StudentDetail',
            fields=[
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('MSSV', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('sex', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(default=None, max_length=50)),
            ],
            options={
                'db_table': 'student_information',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject_Name', models.TextField(max_length=255)),
            ],
            options={
                'db_table': 'subject',
            },
        ),
        migrations.CreateModel(
            name='TeacherDetail',
            fields=[
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('MSGV', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('sex', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(default=None, max_length=50)),
            ],
            options={
                'db_table': 'teacher_information',
            },
        ),
        migrations.CreateModel(
            name='QuestionBank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question_Detail', models.TextField(max_length=99999)),
                ('Question_Image', models.CharField(default=None, max_length=50)),
                ('ID_Subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.subject')),
            ],
            options={
                'db_table': 'question_bank',
            },
        ),
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question_Answer', models.TextField(max_length=99999)),
                ('ID_Question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.questionbank')),
            ],
            options={
                'db_table': 'question_answer',
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Grade', models.CharField(max_length=10)),
                ('ID_Exam', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_admin.exam')),
            ],
            options={
                'db_table': 'grade',
            },
        ),
        migrations.AddField(
            model_name='exam',
            name='ID_Subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.subject'),
        ),
        migrations.AddField(
            model_name='exam',
            name='MSSV',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.studentdetail'),
        ),
        migrations.CreateModel(
            name='CorrectAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Correct_Answer', models.TextField(max_length=99999)),
                ('ID_Question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.questionbank')),
            ],
            options={
                'db_table': 'correct_answer',
            },
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('role', models.CharField(choices=[('A', 'Admin'), ('S', 'Student'), ('T', 'Teacher')], max_length=1)),
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('IDnumber', models.CharField(max_length=50, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Students_Answer',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Students_Answer', models.IntegerField()),
                ('ID_Exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.exam')),
                ('ID_Question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.questionbank')),
            ],
            options={
                'db_table': 'student_answer',
                'unique_together': {('ID_Question', 'ID_Exam')},
            },
        ),
    ]