from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post

        fields = [
            "title",
            "content",
            "category",
            "tags",
            "status",
            "cover_image",
        ]

        widgets = {
            "content": forms.Textarea(
                attrs={
                    "rows": 8,
                    "class": "form-control"
                }
            ),

            "title": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "category": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "status": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "cover_image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control"
                }
            ),
        }

    def clean_title(self):
        title = self.cleaned_data["title"]

        if len(title) < 5:
            raise forms.ValidationError(
                "Title must be at least 5 characters long."
            )

        return title
    
    
# Clean cover image
    def clean_cover_image(self):
        image = self.cleaned_data.get("cover_image")

        if image:
            # Kiểm tra dung lượng tối đa 5MB
            if image.size > 5 * 1024 * 1024:
                raise forms.ValidationError(
                    "Image file too large (max 5MB)."
                )
               # Các định dạng được phép
            valid_extensions = [
                ".jpg",
                ".jpeg",
                ".png",
                ".webp",
            ]

            # Kiểm tra đuôi file
            if not any(
                image.name.lower().endswith(ext)
                for ext in valid_extensions
            ):
                raise forms.ValidationError(
                    "Unsupported file type. Use JPG, PNG, or WEBP."
                )

        return image