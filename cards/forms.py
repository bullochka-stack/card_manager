from django import forms


class SearchForm(forms.Form):
    series = forms.IntegerField(required=False)
    number = forms.IntegerField(required=False)
    created_at = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        }))
    date_end = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker2'
        }))
    use_date = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker3'
        }))
    summa = forms.IntegerField(required=False)
    status = forms.ChoiceField(choices=((None, None),
                                        ('Active', 'Active'),
                                        ('Deactive', 'Deactive'),
                                        ('Overdue', 'Overdue')), required=False)


class GeneratorForm(forms.Form):
    series = forms.IntegerField(min_value=1)
    count = forms.IntegerField(min_value=1)
    period = forms.ChoiceField(choices=(('1 год', '1 год'),
                                        ('6 месяцев', '6 месяцев'),
                                        ('1 месяц', '1 месяц')))
