import elasticsearch
import traceback
from datetime import datetime


elastic = elasticsearch.Elasticsearch(["es.lab.grds.io:9200"])


def add_args(parser):
    parser.add_argument("--createindex", help="Create the ES index for Bug Bounty.", action="store_true")
    parser.add_argument("--esimport", help="Import the workspace into Elasticsearch", action="store_true")


def run(plugins, parser, config):
    parse_args(plugins, parser, config)


def parse_args(plugins, parser, config):
    print(plugins['connect'])
    args = parser.parse_args()

    if args.createindex:
        create_index()

    elif args.esimport:
        return add_host

    else:
        args = parser.parse_args()
        plugins['help'] = True
        return None


def add_host(ip_address, hostname, source, workspace):
    body = {"ip_address": ip_address, "hostname": hostname, "source": source, "workspace": workspace,
            "timestamp": datetime.utcnow()}
    elastic.index(index="bug_bounty", doc_type="host", body=body)


def create_index():
    try:
        host_mapping = {
            "host": {
                "properties": {
                    "ip_address": {"type": "ip"},
                    "source": {"type": "string", "index": "not_analyzed"},
                    "workspace": {"type": "string", "index": "not_analyzed"},
                    "hostname": {"type": "string", "index": "not_analyzed"},
                    "timestamp": {"type": "date"},
                }
            }
        }

        shodan_port_mapping = {
            "shodan_port": {
                "properties": {
                    "ip_address": {"type": "ip"},
                    "source": {"type": "string", "index": "not_analyzed"},
                    "workspace": {"type": "string", "index": "not_analyzed"},
                    "hostname": {"type": "string", "index": "not_analyzed"},
                    "port": {"type": "integer"},
                    "timestamp": {"type": "date"},
                }
            }
        }

        shodan_metadata_mapping = {
            "shodan_metadata": {
                "properties": {
                    "ip_address": {"type": "ip"},
                    "source": {"type": "string", "index": "not_analyzed"},
                    "workspace": {"type": "string", "index": "not_analyzed"},
                    "hostname": {"type": "string", "index": "not_analyzed"},
                    "timestamp": {"type": "date"},
                }
            }
        }

        elastic.indices.create("bug_bounty")
        elastic.indices.put_mapping(index="bug_bounty", doc_type="host", body=host_mapping)
        elastic.indices.put_mapping(index="bug_bounty", doc_type="shodan_port", body=shodan_port_mapping)
        elastic.indices.put_mapping(index="bug_bounty", doc_type="shodan_metadata", body=shodan_metadata_mapping)

    except:
        traceback.print_exc()
