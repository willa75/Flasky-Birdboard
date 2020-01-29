from flask import jsonify, request
from flask_classful import route


from birdboard.extensions import db
from birdboard.api.v1 import V1FlaskView
from birdboard.blueprints.project.models import Project
from birdboard.blueprints.project.schemas import (
    add_project_schema,
    projects_schema
)


class ProjectsView(V1FlaskView):
    def index(self):
        response = {
            'data': {
                'name': 'Batman'
            }
        }

        return jsonify(response), 200

    def post(self):
        json_data = request.get_json()

        if not json_data:
            response = jsonify({'error': 'Invalid Input'})

            return response, 400
        #return json_data, 200
        errors = []
        data = add_project_schema.load(json_data)

        if errors:
            response = {
                'error': errors,
                'data': datax   
            }

            return jsonify(response), 422

        project = Project()
        project.title = data['title']
        project.description = data['description']
        project.save()

        response = {
            'data': {
                'created_on': project.created_on,
                'id': project.id,
                'title': project.title,
                'description': project.description
            }
        }

        return jsonify(response), 200

