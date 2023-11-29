from django import template
from django.template.loader import get_template

register = template.Library()

def my_template(value,arg):
    if arg == 'change':
        value = 'Hussain'
        return value
    if arg == 'title':
        return value.title()

def show_friends():
    friends = [
        {
            'id':1,
            'name':'Bilas',
            'persepective':'was good but not trusted'
        },
        {
            'id':2,
            'name':'Miad',
            'persepective':'not matured'
        },
        {
            'id':3,
            'name':'Shanto',
            'persepective':'trusted'
        }
    ]
    return {'friends':friends}

def show_courses():
    courses =friends = [
        {
            'id':1,
            'name':'Bangla',
            'teacher':'Rahim'
        },
        {
            'id':2,
            'name':'English',
            'teacher':'Karim'
        },
        {
            'id':3,
            'name':'Math',
            'teacher':'Bakar'
        }
    ]
    return {'courses':courses}

friends_template = get_template('first_app/friends.html')
course_template = get_template('first_app/courses.html')
register.filter('change_name',my_template)
register.inclusion_tag(friends_template)(show_friends)
register.inclusion_tag(course_template)(show_courses)