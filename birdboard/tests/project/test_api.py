from flask import url_for

from birdboard.blueprints.project.models import Project
from lib.tests import (
    assert_status_with_message,
    APITestMixin
)


class TestProject(APITestMixin):
    def test_user_can_create_project(self):
        """ Create project successfully. """
        old_project_count = Project.query.count()

        project = {'title': 'Testable Title', 'description':
                'Testable project description.'}
        
        response = self.client.post(url_for('ProjectsView:post'), json=project)

        assert_status_with_message(200, response, "created_on")

        new_project_count = Project.query.count()
        assert (old_project_count + 1) == new_project_count
