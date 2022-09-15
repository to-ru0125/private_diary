from django.views import generic

from .forms import InquiryForm

class IndexView(generic.TemplateView):
    template_name = "blog.html"

class InquiryView(generic.FormView):
    template_name = "inquiry_b.html"
    form_class = InquiryForm
