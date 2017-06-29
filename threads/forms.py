from django import forms
from .models import Thread, Post


class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['name']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['comment']


class ThreadForm(forms.ModelForm):
    name = forms.CharField(label="Thread name")
    is_a_poll = forms.BooleanField(label="Include a poll?", required=False)

    class Meta:
        model = Thread
        fields = ['name']

< script >
$(function()
{
if (!$('#id_is_a_poll'). is ('checked')) {
$('#poll_form').hide()
}

$('#id_is_a_poll').click(function(el)
{
    var
poll_form = $('#poll_form')

if (poll_form. is (":visible"))
{
    poll_form.hide()
} else {
    poll_form.show()
}
})
})
< / script >
