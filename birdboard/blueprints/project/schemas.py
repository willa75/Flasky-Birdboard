from marshmallow import fields, Schema,validate

class ProjectSchema(Schema):
    class Meta:
        fields = ('created_on', 'id', 'description', 'title')


class AddProjectSchema(Schema):
    title = fields.Str(required=True, validate=validate.Length(min=1, max=200))

    description = fields.Str(required=False)


project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)
add_project_schema = AddProjectSchema()