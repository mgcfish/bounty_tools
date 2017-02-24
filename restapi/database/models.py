from datetime import datetime
from restapi.database import db


class Host(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String)
    hostname = db.Column(db.String)
    source = db.Column(db.String)
    workspace = db.Column(db.String)

    def __init__(self, ip_address, hostname, source, workspace):
        self.ip_address = ip_address
        self.hostname = hostname
        self.source = source
        self.workspace = workspace
