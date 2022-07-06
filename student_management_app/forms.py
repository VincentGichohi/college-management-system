
from django import forms
from .models import Courses, SessionYearModel, CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

User = get_user_model()

#A form for registering new users which takes fields
class RegisterForm(forms.ModelForm):
    """
    The default
    """
    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name']

    def clean_email(self, email):
        """
        Verify email is available.
        """
        email = self.cleaned_data(email)
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean_first_name(self, first_name):
        """
        Verify that the first_name field is not blank
        """
        first_name = self.cleaned_data(first_name)
        qs = User.objects.filter(first_name=first_name)
        if qs.exists():
            raise forms.ValidationError("first_name is taken.")
        return first_name

    def clean_last_name(self, last_name):
        """
        Verify that last name is available.
        """
        last_name = self.cleaned_data(last_name)
        qs = User.objects.filter(last_name=last_name)
        if qs.exists():
            raise forms.ValidationError("Last name is taken.")
        return last_name

    def clean(self):
        """
        Verify both passwords match
        """
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_2 = cleaned_data.get('password_2')
        if password is not None and password != password_2:
            self.add_error('Password_2', "Your passwords must match")
        return cleaned_data


#A form for logging in new users. Checks the email and their passwords
class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required fields, 
    plus a repeated password.
    """
    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['email']

    def clean(self):
        """
        Verify both passwords match.
        """
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords do not match.")
        return cleaned_data

    def save(self, commit=True):
        # Save the provided password in hashed format.
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """
    A form for updating users. Includes all fields on the user,
    but replaces the password field with admin's password hash
    display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'is_active']

    def clean_password(self):
        # Regardless of what the user provides, return the initial value
        # This is done here, rather than one of the field, because the
        # field does not have access to the initial value
        return self.initial['password']


class DateInput(forms.DateInput):
    input_type = "date"
 
 
class AddStudentForm(forms.Form):
    email = forms.EmailField(label="Email",
                             max_length=50,
                             widget=forms.EmailInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Password",
                               max_length=50,
                               widget=forms.PasswordInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name",
                                 max_length=50,
                                 widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name",
                                max_length=50,
                                widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username",
                               max_length=50,
                               widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(label="Address",
                              max_length=50,
                              widget=forms.TextInput(attrs={"class":"form-control"}))
 
    #For Displaying Courses
    try:
        courses = Courses.objects.all()
        course_list = []
        for course in courses:
            single_course = (course.id, course.course_name)
            course_list.append(single_course)
    except:
        print("here")
        course_list = []
     
    # For Displaying Session Years
    try:
        session_years = SessionYearModel.objects.all()
        session_year_list = []
        for session_year in session_years:
            single_session_year = (session_year.id, str(session_year.session_start_year)+" to "+str(session_year.session_end_year))
            session_year_list.append(single_session_year)
             
    except:
        session_year_list = []
     
    gender_list = (
        ('Male','Male'),
        ('Female','Female')
    )
     
    course_id = forms.ChoiceField(label="Course",
                                  choices=course_list,
                                  widget=forms.Select(attrs={"class":"form-control"}))
    gender = forms.ChoiceField(label="Gender",
                               choices=gender_list,
                               widget=forms.Select(attrs={"class":"form-control"}))
    session_year_id = forms.ChoiceField(label="Session Year",
                                        choices=session_year_list,
                                        widget=forms.Select(attrs={"class":"form-control"}))
    profile_pic = forms.FileField(label="Profile Pic",
                                  required=False,
                                  widget=forms.FileInput(attrs={"class":"form-control"}))

            
class EditStudentForm(forms.Form):
    email = forms.EmailField(label="Email",
                             max_length=50,
                             widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name",
                                 max_length=50,
                                 widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name",
                                max_length=50,
                                widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username",
                               max_length=50,
                               widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(label="Address",
                              max_length=50,
                              widget=forms.TextInput(attrs={"class":"form-control"}))
 
    # For Displaying Courses
    try:
        courses = Courses.objects.all()
        course_list = []
        for course in courses:
            single_course = (course.id, course.course_name)
            course_list.append(single_course)
    except:
        course_list = []
 
    # For Displaying Session Years
    try:
        session_years = SessionYearModel.objects.all()
        session_year_list = []
        for session_year in session_years:
            single_session_year = (session_year.id, str(session_year.session_start_year)+" to "+str(session_year.session_end_year))
            session_year_list.append(single_session_year)
             
    except:
        session_year_list = []
 
     
    gender_list = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
     
    course_id = forms.ChoiceField(label="Course",
                                  choices=course_list,
                                  widget=forms.Select(attrs={"class":"form-control"}))
    gender = forms.ChoiceField(label="Gender",
                               choices=gender_list,
                               widget=forms.Select(attrs={"class":"form-control"}))
    session_year_id = forms.ChoiceField(label="Session Year",
                                        choices=session_year_list,
                                        widget=forms.Select(attrs={"class":"form-control"}))
    profile_pic = forms.FileField(label="Profile Pic",
                                  required=False,
                                  widget=forms.FileInput(attrs={"class":"form-control"}))


