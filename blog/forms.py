from django import forms


CATEGORIES = [
    ('', '▼お問い合わせ内容を以下から選択してください▼'),
    ('business_request', 'お仕事の依頼'),
    ('site_inquiry', 'サイト内容に関する問い合わせ'),
    ('etc', 'その他'),
]

class ContactForm(forms.Form):
    category = forms.ChoiceField(
        label='',
        choices=CATEGORIES,
        widget=forms.Select(attrs={
            'class': 'form-select',
        }),
    )
    subject = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "お名前",
        }),
    )
    sender = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': "メールアドレス",
        }),
    )
    message = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': "お問い合わせ内容の詳細",
        }),
    )
