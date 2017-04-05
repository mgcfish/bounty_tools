#!/usr/bin/env python

import argparse
from os import listdir
from importlib import import_module

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Command line tool for bounty management.")
    parser.add_argument("--connect", help="Manage connectivity.")
    parser.add_argument("--report", help="Report on the data.")
    parser.add_argument("--recon", help="Run recon tasks.")
    parser.add_argument("--store", help="Manage where data is persisted.")
    args = parser.parse_args()

    plugins = {"recon": {}, "connect": {}, "store": {}, "report": {}}

    # Load plugins
    plugin_types = ['recon', 'connect', 'store', 'report']
    for plugin_type in plugin_types:
        for file_name in listdir(plugin_type):
            if not file_name.startswith('_') and file_name.endswith('.py'):
                module_name = file_name.replace('.py', '')
                plugins[plugin_type][module_name] = import_module(plugin_type + '.' + module_name)

    # Process arguments in order of requirements: connectivity, recon, datastore, reporting
    if args.connect is not None:
        if args.connect in plugins['connect'].keys():
            args.connect = plugins['connect'][args.connect].run()

    if args.store is not None:
        pass

    if args.recon is not None:
        pass

    if args.report is not None:
        pass

