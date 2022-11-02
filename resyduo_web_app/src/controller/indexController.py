from flask import render_template, redirect, url_for, request, flash

from service.tag_service import TagService

tag_service = TagService()

def index(name=None,tag=None,components=None):
    
    name='ReSyDuo'
    all_tags = tag_service.getAll()
    tag = 'test'
    if tag:
        components = ['comp1','comp2']
    tag_list = ['tag1','tag5','tag3','tag4']
    return render_template('index.html', name=name,tag_list=all_tags,components=components)