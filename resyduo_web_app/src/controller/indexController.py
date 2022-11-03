from flask import render_template, redirect, url_for, request, flash

from service.tag_service import TagService
from service.component_service import ComponentService

tag_service = TagService()
component_service = ComponentService()

def index(name=None):
    name='ReSyDuo'
    all_tags = tag_service.getAll()
    all_components = component_service.getAll()
    l=[]
    l.append(list(component_service.components_predictions.keys())[0])
    l.append(list(component_service.components_predictions.keys())[1])
    l.append(list(component_service.components_predictions.keys())[3])
    result=component_service.get_libs_by_component_id_list(l)
    print(result)
    return render_template('base.html', name=name,all_tags=all_tags,all_components=all_components)