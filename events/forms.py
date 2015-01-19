from django import forms
from django.forms import ModelForm

from .models import Event

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Fieldset, ButtonHolder, Field, Button


event_fields = ['title', 'description', 'start', 'end', 'location']


class EventBaseForm(ModelForm):
    start = forms.DateTimeField(
        widget=forms.TextInput(
            attrs={
                'placeholder': '2015-01-25 10:00'
            }
        ),
        label="Start Datetime",
        help_text="Sorry, start and end datetime are going to be weird for now." + \
        " Please enter in the format listed above."
    )
    end = forms.DateTimeField(
        widget=forms.TextInput(
            attrs={
                'placeholder': '2015-01-25 14:00'
            }
        ),
        label="Start Datetime",
    )
    description = forms.CharField(widget=forms.Textarea, required=False)
    location = forms.CharField(help_text="Address, place name, etc", required=False)

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
    form_title = '<h1 class="text-center">Create New Event</h1>'
    btn_text = 'Create New Event'


class EventUpdateForm(EventBaseForm):
    form_title = '<h1 class="text-center">Update Event</h1>'
    btn_text = 'Update Event'