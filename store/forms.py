from django import forms

class QandAForms(forms.Form):
    question = forms.CharField(max_length=100, required=True)
    
"""
    def __init__(self, user, *args, **kwargs):
        super(QandAForms, self).__init__(*args, **kwargs)
        self.fields['user'].initial = user
        self.fields['user'].disabled = True
"""        
    
class AnswerForm(forms.Form):
    answer = forms.CharField(max_length=250, required=True)