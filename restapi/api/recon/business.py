from restapi.database import db
from restapi.database.models import Host


def create_host(data):
    ip_address = data.get('ip_address')
    hostname = data.get('hostname')
    source = data.get('source')
    workspace = data.get('workspace')

    host = Host(ip_address, hostname, source, workspace)
    db.session.add(host)
    db.session.commit()
