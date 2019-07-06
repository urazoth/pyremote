#!/usr/bin/env python
import argparse
import operations


def main():
    parser = argparse.ArgumentParser(description='Tool to remember remote ssh hosts')
    
    parser.add_argument('alias', nargs='?', metavar='alias', type=str, help='Alias to connect')

    group_main = parser.add_mutually_exclusive_group()
    group_main.add_argument('-list', action='store_true', help='List saved hosts')
    group_main.add_argument('-add', action='store_true', help='Adds new host')
    group_main.add_argument('-show', metavar='alias', help='Show alias configuration')

    group_add = parser.add_argument_group('add')
    group_add.add_argument('--alias', metavar='', type=str, help='Hosts alias (one word)')
    group_add.add_argument('--host', metavar='', type=str, help='Host ip or domain')
    group_add.add_argument('--key-path', metavar='', type=str, help='File with public key')
    group_add.add_argument('--login', metavar='', type=str, help='Login to remote host')

    parser.add_argument('--autocompletion', type=str, help=argparse.SUPPRESS)

    args = parser.parse_args()

    if args.alias:
        operations.run_ssh(args.alias)

    if args.list:
        operations.list_saved_hosts()
        return
    
    if args.show:
        operations.show(args.show)
        return
    
    if args.add:
        operations.add_new_host(args.alias, args.host, args.key_path, args.login)
        return


if __name__ == "__main__":
    main()
