from django import forms

class CourseDetailsForm(forms.Form):
    courseID = forms.CharField(label='Course ID', required=True,
                               widget=forms.TextInput(attrs={'style': 'width: 300px;'})
                               )
    
    courseName = forms.CharField(label='Course Name', required=True,
                                 widget=forms.TextInput(attrs={'style': 'width: 700px;'})
                                 )
    
    semester = forms.CharField(label='Semester', required=True,
                               widget=forms.TextInput(attrs={'style': 'width: 200px;'})
                               )

    EXAM_CATEGORY_CHOICES = [
        ('Mid-term', 'Mid-term'),
        ('End-term', 'End-term'),
    ]
    term = forms.ChoiceField(
        label='Exam Category',
        widget=forms.RadioSelect,
        choices=EXAM_CATEGORY_CHOICES,
        required=True
    )
