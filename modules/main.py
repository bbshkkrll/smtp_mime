from _socket import gaierror

from argparse import ArgumentParser

from smtp_client import Client

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-f', '--from', type=str, default='<>', dest='sender')
    parser.add_argument('-t', '--to', type=str)
    parser.add_argument('-d', '--directory', type=str, default='.')
    parser.add_argument('--subject', type=str, default='Happy pictures')
    parser.add_argument('-s', '--server', type=str, default='smtp.mail.ru:25')
    parser.add_argument('--ssl', action='store_true')
    parser.add_argument('--auth', action='store_true')
    parser.add_argument('-v', '--verbose', action='store_true')

    args = parser.parse_args()
    try:
        client = Client(args.sender, args.to, args.subject, args.ssl, args.auth, args.verbose, args.directory,
                        args.server)
        client.run()
    except ValueError as e:
        print(e)
    except gaierror:
        print('DNS Error')
    except ConnectionError:
        print('Connection error')
