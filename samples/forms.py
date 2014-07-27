from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import *

from autofill.models import AutoFill
from samples.models import MetaData
from samples.forms_constants import *

class SampleMetaDataForm(forms.Form):

    def _query_autofill(self, user_id):
        query = AutoFill.objects.all().filter(user_id=user_id)
        self.saved_settings = {}
        for row in query:
            if row.field in FIELDS:
                self.saved_settings[row.field] = row.value

    def __init__(self, user_id, *args, **kwargs):
        self._query_autofill(user_id)
        super(SampleMetaDataForm, self).__init__(*args, **kwargs)
        
        for id in FIELD_ORDER:
            value = self.saved_settings[id] if id in self.saved_settings else ''
            widget_attrs = {
                'placeholder':FIELDS[id][1],
                'value':value,
            }
            attributes = {                    
                'label':FIELDS[id][0],            
                'required':True if id in REQUIRED_FIELDS else False,
            }
            if id.endswith('_email'):
                attributes['widget'] = forms.EmailInput(attrs=widget_attrs)
                self.fields[id] = forms.EmailField(**attributes)
            elif id.endswith('_link'):
                attributes['widget'] = forms.URLInput(attrs=widget_attrs)
                self.fields[id] = forms.URLField(**attributes)
            elif id.endswith('_date'):
                attributes['widget'] = forms.DateInput(attrs=widget_attrs)
                self.fields[id] = forms.DateField(**attributes)
            elif id.startswith('is_'):
                if id == 'is_public':
                    widget_attrs['checked'] = 'checked'
                attributes['widget'] = forms.CheckboxInput(attrs=widget_attrs)
                self.fields[id] = forms.BooleanField(**attributes)
            elif id in SELECT_FIELDS:
                attributes['widget'] = forms.Select(attrs=widget_attrs)
                self.fields[id] = forms.ChoiceField(choices=CHOICES[id], **attributes)
            elif id == 'sequence_file':
                attributes['widget'] = forms.ClearableFileInput(attrs=widget_attrs)
                self.fields[id] = forms.FileField(**attributes)
            else:
                if id == 'comments':
                    attributes['widget'] = forms.Textarea(attrs=widget_attrs)
                else:
                    attributes['widget'] = forms.TextInput(attrs=widget_attrs)
                self.fields[id] = forms.CharField(**attributes)

        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_id = 'submit-sample'
        self.helper.form_class = ''
        self.helper.form_action = ''
        self.helper.layout = Layout()
        
        self.helper.layout.extend(self.fields)
        
        offset = 'col-sm-offset-2 col-md-offset-3'
        tab_css = 'col-sm-8 col-md-6 ' + offset
        self.helper.layout.insert(0, 'Project Information')
        self.helper[0:9].wrap_together(Tab, css_class=tab_css)
        self.helper.layout.insert(1, 'Publication Information')
        self.helper[1:7].wrap_together(Tab, css_class=tab_css)
        self.helper.layout.insert(2, 'Organism Information')
        self.helper[2:13].wrap_together(Tab, css_class=tab_css)
        self.helper.layout.insert(3, 'Phenotype Information')
        self.helper[3:15].wrap_together(Tab, css_class=tab_css)
        self.helper.layout.insert(4, 'Sequence Information')
        self.helper[4:8].wrap_together(Tab, css_class=tab_css)

        self.helper[0:5].wrap_together(TabHolder)
        self.helper.add_input(Submit('submit', 'Submit Sample', css_class=offset))
  