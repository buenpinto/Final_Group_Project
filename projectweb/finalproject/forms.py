# In this section we import the dictionaries defined in modules.py
# and define all the forms we will use in views.py

from django import forms
from .models import Input, REGION, CAT, VAR, C1, C2, C3, C4, C5 , C6, C7, C8, C9, C10, C11, C12, C13

############################### REGION FORM ####################################
class InputForm(forms.ModelForm):

    attrs = {'class ' : 'form−control ',
             'onchange ' : 'this.form.submit() '}

    region = forms.ChoiceField(choices=REGION, required=False,
                              widget=forms.Select(attrs = attrs))

    #cat = forms.ChoiceField(choices=CAT, required=False,
    #                             widget=forms.Select(attrs = attrs))

    class Meta:

        model = Input
        fields = ['region']

########## DUAL FORM: region + edu_pov(Education/Poverty) #####################

# This is the (dual) form used on the Cross Sectional Plots section

class REG_VAR(forms.ModelForm):

    attrs = {'class ' : 'form−control ',
             'onchange ' : 'this.form.submit() '}

    region = forms.ChoiceField(choices=REGION, required=False,
                                  widget=forms.Select(attrs = attrs))


    edu_pov = forms.ChoiceField(choices=VAR, required=False,
                                  widget=forms.Select(attrs = attrs))


    class Meta:

        model = Input
        fields = ['region','edu_pov']


########## DUAL FORM: county1 + cat(Poverty/Income) ###########################

# The following (dual) forms, from C1 to C13, are used on the Time series plots section

class C1(forms.ModelForm):

    attrs = {'class ' : 'form−control ',
             'onchange ' : 'this.form.submit() '}

    c1 = forms.ChoiceField(choices=C1, required=False,
                                  widget=forms.Select(attrs = attrs))

    cat = forms.ChoiceField(choices=CAT, required=False,
                                     widget=forms.Select(attrs = attrs), initial='1')

    class Meta:

        model = Input
        fields = ['c1', 'cat']



class C2(forms.ModelForm):

    attrs = {'class ' : 'form−control ',
             'onchange ' : 'this.form.submit() '}

    c2 = forms.ChoiceField(choices=C2, required=False,
                                  widget=forms.Select(attrs = attrs))

    cat = forms.ChoiceField(choices=CAT, required=False,
                                     widget=forms.Select(attrs = attrs))

    class Meta:

        model = Input
        fields = ['c2']




class C3(forms.ModelForm):

    attrs = {'class ' : 'form−control ',
             'onchange ' : 'this.form.submit() '}

    c3 = forms.ChoiceField(choices=C3, required=False,
                                  widget=forms.Select(attrs = attrs))

    cat = forms.ChoiceField(choices=CAT, required=False,
                                     widget=forms.Select(attrs = attrs))

    class Meta:

        model = Input
        fields = ['c3']



class C4(forms.ModelForm):

    attrs = {'class ' : 'form−control ',
             'onchange ' : 'this.form.submit() '}

    c4 = forms.ChoiceField(choices=C4, required=False,
                                  widget=forms.Select(attrs = attrs))

    cat = forms.ChoiceField(choices=CAT, required=False,
                                     widget=forms.Select(attrs = attrs))


    class Meta:

        model = Input
        fields = ['c4']



class C5(forms.ModelForm):

    attrs = {'class ' : 'form−control ',
             'onchange ' : 'this.form.submit() '}

    c5 = forms.ChoiceField(choices=C5, required=False,
                                  widget=forms.Select(attrs = attrs))

    cat = forms.ChoiceField(choices=CAT, required=False,
                                     widget=forms.Select(attrs = attrs))

    class Meta:

        model = Input
        fields = ['c5']


class C6(forms.ModelForm):

    attrs = {'class ' : 'form−control ',
             'onchange ' : 'this.form.submit() '}

    c6 = forms.ChoiceField(choices=C6, required=False,
                                  widget=forms.Select(attrs = attrs))

    cat = forms.ChoiceField(choices=CAT, required=False,
                                     widget=forms.Select(attrs = attrs))


    class Meta:

        model = Input
        fields = ['c6']


class C7(forms.ModelForm):

    attrs = {'class ' : 'form−control ',
             'onchange ' : 'this.form.submit() '}

    c7 = forms.ChoiceField(choices=C7, required=False,
                                  widget=forms.Select(attrs = attrs))

    cat = forms.ChoiceField(choices=CAT, required=False,
                                     widget=forms.Select(attrs = attrs))


    class Meta:

        model = Input
        fields = ['c7']




class C8(forms.ModelForm):

    attrs = {'class ' : 'form−control ',
             'onchange ' : 'this.form.submit() '}

    c8 = forms.ChoiceField(choices=C8, required=False,
                                  widget=forms.Select(attrs = attrs))

    cat = forms.ChoiceField(choices=CAT, required=False,
                                     widget=forms.Select(attrs = attrs))


    class Meta:

        model = Input
        fields = ['c8']




class C9(forms.ModelForm):

    attrs = {'class ' : 'form−control ',
             'onchange ' : 'this.form.submit() '}

    c9 = forms.ChoiceField(choices=C9, required=False,
                                  widget=forms.Select(attrs = attrs))


    cat = forms.ChoiceField(choices=CAT, required=False,
                                     widget=forms.Select(attrs = attrs))

    class Meta:

        model = Input
        fields = ['c9']




class C10(forms.ModelForm):

    attrs = {'class ' : 'form−control ',
             'onchange ' : 'this.form.submit() '}

    c10 = forms.ChoiceField(choices=C10, required=False,
                                  widget=forms.Select(attrs = attrs))

    cat = forms.ChoiceField(choices=CAT, required=False,
                                     widget=forms.Select(attrs = attrs))


    class Meta:

        model = Input
        fields = ['c10']



class C11(forms.ModelForm):

    attrs = {'class ' : 'form−control ',
             'onchange ' : 'this.form.submit() '}

    c11 = forms.ChoiceField(choices=C11, required=False,
                                  widget=forms.Select(attrs = attrs))


    cat = forms.ChoiceField(choices=CAT, required=False,
                                     widget=forms.Select(attrs = attrs))

    class Meta:

        model = Input
        fields = ['c11']



class C12(forms.ModelForm):

    attrs = {'class ' : 'form−control ',
             'onchange ' : 'this.form.submit() '}

    c12 = forms.ChoiceField(choices=C12, required=False,
                                  widget=forms.Select(attrs = attrs))

    cat = forms.ChoiceField(choices=CAT, required=False,
                                     widget=forms.Select(attrs = attrs))

    class Meta:

        model = Input
        fields = ['c12']



class C13(forms.ModelForm):

    attrs = {'class ' : 'form−control ',
             'onchange ' : 'this.form.submit() '}

    c13 = forms.ChoiceField(choices=C13, required=False,
                                  widget=forms.Select(attrs = attrs))

    cat = forms.ChoiceField(choices=CAT, required=False,
                                     widget=forms.Select(attrs = attrs))


    class Meta:

        model = Input
        fields = ['c13']
