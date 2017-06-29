import arrow
from django import template
from django.core.urlresolvers import reverse

register = template.Library()



@register.filter
def started_time(created_at):
    return arrow.get(created_at).humanize()


@register.simple_tag
def last_posted_user_name(thread):
    posts = thread.posts.all().order_by('-created_at')
    return posts[posts.count() - 1].user.username


@register.filter
def vote_percentage(subject):
   count = subject.votes.count()
   if count == 0:
       return 0
   total_votes = subject.poll.votes.count()
   return (100 / total_votes) * count
