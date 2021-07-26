import csv
import os

from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse, request
from .models import CourseContent, Prof, Spec


# Create your views here.
# def HomePage(request):
#     return HttpResponse("Hey Mara")

class HomePage(ListView):
    model = CourseContent
    template_name = 'home.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.import_csvs()

    def import_csvs(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))

        specs = []
        lecturers = []

        with open(dir_path + '/professors_tab.tsv', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter="\t")
            # Professor,Description,Specialization
            # Professor	Description	Specializations	FOMO

            for i, row in enumerate(reader):

                if i == 0:
                    continue

                spec = Spec()
                spec.special=row[2]
                spec.FOMO=row[3]
                spec.save()
                specs.append(spec)

        with open(dir_path + '/professors_tab.tsv', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter="\t")
            # Professor,Description,Specialization
            # Professor	Description	Specializations	FOMO

            for i, row in enumerate(reader):

                if i == 0:
                    continue

                x = Prof()
                x.prof = row[0]
                x.description = row[1]
                for item in specs:
                    if row[2] == item.special:
                        x.specialisation = item
                        break

                x.save()
                lecturers.append(x)

        with open(dir_path + '/course_list_tab.tsv', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter="\t")
            # Number,Title,Faculty,Semester,Section,Credits,Modality**

            for i, row in enumerate(reader):

                if i == 0:
                    continue

                faculty = ""
                if ";" in row[2]:
                    x = row[2].split(";")
                    for item in x:
                        faculty += item
                else:
                    faculty = row[2]

                found = False
                for item in lecturers:
                    if faculty in item.prof or item.prof in faculty:
                        faculty = item
                        found = True
                        break
                if not found:
                    faculty = None

                x = CourseContent()

                x.ID = row[0]
                x.title = row[1]
                x.faculty = faculty
                x.semester = row[3]
                x.section = row[4]
                x.course_credits = row[5]
                x.modality = row[6]
                x.save()


