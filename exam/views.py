from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
from .models import (
    Soal,
    KombinasiSoal
)


class UjianView(TemplateView):
    template_name = 'exam/ujian.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        soal = Soal.objects.all()
        kombinasi = KombinasiSoal.objects.all()
        context['soal'] = soal
        context['kombinasi'] = kombinasi

        from django.core.serializers import serialize
        data = serialize("json", soal)
        data_kombinasi = serialize("json", kombinasi)
        context["data"] = data
        context['data_kombinasi'] = data_kombinasi

        return self.render_to_response(context)
