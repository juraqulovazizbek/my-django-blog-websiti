from uuid import uuid4

from django import forms


class BlogCreateForm(forms.Form):
    title = forms.CharField(min_length=1, max_length=128)
    reading_minute = forms.IntegerField(min_value=1, max_value=120)
    content = forms.CharField(min_length=1)
    tg_link = forms.URLField()
    is_published = forms.BooleanField(required=False)
    # created_at = 9
    # updated_at = 12

    #field form
    def clean_title(self):
        data: str = self.cleaned_data["title"]

        if not data.isalpha():
            raise forms.ValidationError('eyuuuu')
        
        return data
    # #object form
    # def clean(self):
    #     data = self.cleaned_data

    #     if data['created_at'] > data['updated_at']:
    #         raise forms.ValidationError('veeyuuu')
    #     return super().clean()
    

class BlogSearchForm(forms.Form):
    search = forms.CharField(min_length=5, max_length=30)
