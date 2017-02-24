import logging

from flask import request
from flask_restplus import Resource
from restapi.api.recon.business import create_host
from restapi.api.recon.serializers import host, page_of_hosts
from restapi.api.recon.parsers import pagination_arguments
from restapi.api.restplus import api
from restapi.database.models import Host


log = logging.getLogger(__name__)

ns = api.namespace('recon/hosts', description="Operations related to hosts")


@ns.route('/')
class HostsCollection(Resource):
    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_hosts)
    def get(self):
        """
        :return: a list of Hosts
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        hosts_query = Host.query
        hosts_page = hosts_query.paginate(page, per_page, error_out=False)

        return hosts_page

    @api.expect(host)
    def post(self):
        """
        Creates a new Host
        """
        create_host(request.json)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Host not found.')
class HostItem(Resource):
    @api.marshal_with(host)
    def get(self, id):
        """
        :param id:
        :return: a host
        """
        return Host.query.filter(Host.id == id).one()
