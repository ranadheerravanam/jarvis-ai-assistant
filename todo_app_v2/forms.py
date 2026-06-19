from django import forms

class TodoForm(forms.Form):
    title = forms.CharField(max_length=200, required=True)
    description = forms.CharField(max_length=500, widget=forms.Textarea)
    priority = forms.IntegerField(min_value=1, max_value=5)

class UpdateTodoForm(forms.ModelForm):
    class Meta:
        model = 'Todo'
        fields = ['title', 'description']