import base64
import click
import quali_proc.mirror as mirror

@click.command()
@click.option(
    "--port",
    default="21",
    type=str,
    required=True,
    help="Port used for connecting to FTP server."
)
@click.option(
    "--results_path",
    default="data/results",
    type=str,
    required=False,
    help="Path to store results mirrored from FTP server."
)
@click.argument("ftpasswd", type=click.File("rb"))
@click.argument("host_address", nargs=1)
@click.argument("game_port", nargs=1)
def proc(port, results_path, ftpasswd, host_address, game_port):
    """\b
    FTPASSWD        base64 file w/ the FTP username and password.
    HOST_ADDRESS    IP or FQDN of the FTP server.
    GAME_PORT       Port used by ACC server.
    """
    user, password = base64.b64decode(ftpasswd.read()).split(b",")
    game_server_root = "_".join([host_address, game_port])
    game_results_path = "/".join([game_server_root, "results"])
    server = mirror.connect(user.decode("ascii"),
        password.decode("ascii"), port, host_address)
    game_results_list = mirror.get_results_list(server, game_results_path)
    mirror.bulk_download(server, game_results_list, game_results_path, results_path)
    server.close()

if __name__ == "__main__":
    proc()
