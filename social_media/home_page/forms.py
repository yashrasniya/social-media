from django import forms
from .models import Post
MAX_LENGTH=200
class post_upload(forms.ModelForm):
    class Meta:
        model = Post
        fields= ['post_description','photo']
    def clear_content(self):
        content= self.cleaned_data.get("post_description")
        if len(content)>MAX_LENGTH:
            raise forms.ValidationError("post_discription is very long")
        return content


