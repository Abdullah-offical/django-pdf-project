from django import forms
from django.forms.widgets import ClearableFileInput

class Pdf2WordForm(forms.Form):
    pdf_doc = forms.FileField(
        label='Select PDF',
        widget=forms.FileInput(
            attrs = {'accept' : 'application/pdf'} # only upload pdf form
        ),
        required=True
    )


class Pdf2CSVForm(forms.Form):
    pdf_doc = forms.FileField(
        label='Select PDF',
        widget=forms.FileInput(
            attrs = {'accept' : 'application/pdf'} # only upload pdf form
        ),
        required=True
    )


class MultipleFileInput(ClearableFileInput):
    allow_multiple_selected = True

class MergePdfForm(forms.Form):
    pdf_doc = forms.FileField(
        label='Select PDFs',
        widget=MultipleFileInput(
            attrs={'multiple': True, 'accept': 'application/pdf'}
        ),
        required=True
    )


from django import forms

class SplitForm(forms.Form):
    pdf_doc = forms.FileField(
        label='Select a PDF document to upload',
        widget=forms.ClearableFileInput(
            attrs={'accept': 'application/pdf'}
        ),
        required=True
    )
    pg_form = forms.IntegerField(
        required=True, 
        min_value=1,
        label='Page From'
    )
    pg_to = forms.IntegerField(
        required=True, 
        min_value=1,
        label='Page To'
    )


class PDFLockForm(forms.Form):
    pdf_doc = forms.FileField(
        label='Seleact a PDf documenet to upload',
        widget=forms.ClearableFileInput(attrs={
            'accept': 'application/pdf'
        }),
    )
    lock_pdf = forms.CharField(required=True,max_length=64, widget=forms.PasswordInput, label='Pdf lock Password')
    confirm_pdf = forms.CharField(required=True,max_length=64, widget=forms.PasswordInput, label='Pdf lock Confirm Password')

class PDFUnlockForm(forms.Form):
    pdf_doc = forms.FileField(
        label='Seleact a PDf documenet to upload',
        widget=forms.ClearableFileInput(attrs={
            'accept': 'application/pdf'
        }),
    )
    un_pwd = forms.CharField(required=True,max_length=64, widget=forms.PasswordInput, label='Pdf unlock Password')
    