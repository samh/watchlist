from django.forms import forms


class ProgressWidget(forms.TextInput):
    def __init__(self, attrs=None):
        if not attrs:
            attrs = {}
        attrs['class'] = 'progress' + attrs.get('class', '')
        super(ProgressWidget, self).__init__(attrs)
        
    class Media:
        css = {
            'all': ('css/progress_widget.css',)
        }
        js = ('js/jquery-1.6.4.min.js', 'js/progress_widget.js',)
