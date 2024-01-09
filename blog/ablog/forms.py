from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','header_image','body')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control','id':'title'}),
			'body': forms.Textarea(attrs={'class': 'form-control','id':'body'}),					
		}
                

		def clean(self):
                    super(PostForm, self).clean()
                    title = self.cleaned_data.get('title')
                    text = self.cleaned_data.get('body')
                    if len(title) < 5:
                      self._errors['title'] = self.error_class(['Minimum 5 characters required'])
                    if len(text) <10:
                      self._errors['body'] = self.error_class(['Post Should Contain a minimum of 10 characters'])
                    return self.cleaned_data
              


              
                

        
              