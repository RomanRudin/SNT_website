from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.admin.widgets import FilteredSelectMultiple    
from django.contrib.auth.models import Group

User = get_user_model()


# Create ModelForm based on the Group model.
class GroupAdminForm(forms.ModelForm):
    class Meta:
        model = Group
        exclude = []

    # Add the users field.
    users = forms.ModelMultipleChoiceField(
         queryset=User.objects.all(), 
         required=False,
         # Use the pretty 'filter_horizontal widget'.
         widget=FilteredSelectMultiple('users', False)
    )

    def __init__(self, *args, **kwargs):
        # Do the normal form initialisation.
        super(GroupAdminForm, self).__init__(*args, **kwargs)
        # If it is an existing group (saved objects have a pk).
        if self.instance.pk:
            # Populate the users field with the current Group users.
            self.fields['users'].initial = self.instance.user_set.all()

    def save_m2m(self):
        # Add the users to the Group.
        self.instance.user_set.set(self.cleaned_data['users'])

    def save(self, *args, **kwargs):
        # Default save
        instance = super(GroupAdminForm, self).save()
        # Save many-to-many data
        self.save_m2m()
        return instance
    

class WaterSubmissionForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.water_meter = kwargs.pop('water_meter', None)
        super(WaterSubmissionForm, self).__init__(*args, **kwargs)

    value = forms.IntegerField(help_text="Укажите показание счетчика")

    def clean_value(self):
        data = self.cleaned_data['value']

        last_submission = self.water_meter.water_submissions().last()
        last_submission_value = last_submission.value if last_submission is not None else 0

        if data <= last_submission_value:
            raise ValidationError('Показания должны быть больше предыдущего значения')
        
        return data
