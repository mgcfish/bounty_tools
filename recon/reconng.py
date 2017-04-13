def add_args(parser):
    pass


def run(plugins, parser, config):
    parse_args(plugins, parser, config)


def parse_args(plugins, parser, config):
    args = parser.parse_args()
    plugins['help'] = True
    return None

