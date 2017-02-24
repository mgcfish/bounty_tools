from flask_restplus import fields
from restapi.api.restplus import api

host = api.model('Host', {
    'id': fields.Integer(readOnly=True, description="The unique identifier of a host."),
    'ip_address': fields.String(required=True, description="The IP address."),
    'hostname': fields.String(required=True, description="The hostname."),
    'source': fields.String(required=True, description="What tool was used to discover this host."),
    'workspace': fields.String(required=True, description="What workspace this host was discovered under."),
})


pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})


page_of_hosts = api.inherit('Page of hosts', pagination, {
    'items': fields.List(fields.Nested(host))
})


category = api.model('Host category', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a host category'),
    'name': fields.String(required=True, description='Category name'),
})


category_with_hosts = api.inherit('Host category with hosts', category, {
    'hosts': fields.List(fields.Nested(host))
})
