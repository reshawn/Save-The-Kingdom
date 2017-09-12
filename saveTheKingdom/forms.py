from django.forms import ModelForm
from .models import Wanderer

class newWanderer(ModelForm):
    def clean_name(self):
        return self.cleaned_data['name']

    def clean_comment(self):
        return self.cleaned_data['comment']

    # def __init__(self, *args, **kwargs):
    #     # first call parent's constructor
    #     super(newWanderer, self).__init__(*args, **kwargs)
    #     # there's a `fields` property now
    #     self.fields['name'].required = False
    
    class Meta:
        model = Wanderer
        fields = ['name','comment']
        labels = {'name': 'Nickname', 'comment': 'Quote/Story   '}
        help_texts = {'name': 'Who is this person known as?', 'comment': 'Inspirational quote or a background story'}


