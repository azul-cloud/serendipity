from django import forms
from django.forms import ModelForm

from .models import Event

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Fieldset, ButtonHolder, Field, Button


event_fields = ['title', 'description', 'start', 'end', 'location']


class EventBaseForm(ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(EventBaseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                self.form_title,
                Div('title', css_class="col-sm-6 col-sm-offset-3"),
                Div('description', css_class="col-sm-12"),
                Div('start', css_class="col-sm-6"),
                Div('end', css_class="col-sm-6"),
                Div('location', css_class="col-sm-6"),
            ),
            ButtonHolder(
                Submit('submit', self.btn_text, css_class='btn-lg'),
                css_class = "text-center",
            ),
        )

    class Meta:
        model = Event
        fields = event_fields


class EventCreateForm(EventBaseForm):
    form_title = '<h1>Create New Event</h1>'
    btn_text = 'Create New Event'


class EventUpdateForm(EventBaseForm):
    form_title = '<h1>Update Event</h1>'
    btn_text = 'Update Event'