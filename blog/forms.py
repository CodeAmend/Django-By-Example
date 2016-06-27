from django import forms


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    # todo: why not make comments - forms.Textarea() ??? why widget??
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)

