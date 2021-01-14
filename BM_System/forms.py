from django import forms

# お問い合わせフォーム作成用
class ContactForm(forms.Form):
    name = forms.CharField(label='お名前', max_length=50)
    email = forms.EmailField(label='メールアドレス', help_text='※ご確認の上、正しく入力してください。')
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)
    myself = forms.BooleanField(label='内容を受け取る', required=False)

