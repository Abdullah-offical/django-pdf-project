from django import forms

class Pdf2WordForm(forms.Form):
    pdf_doc = forms.FileField(
        widget=forms.FileInput(
            attrs = {'accept' : 'application/pdf'} # only upload pdf form
        ),
        required=True
    )