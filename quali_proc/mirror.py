from ftpretty import ftpretty

def get_results_list(server, path):
    file_list = server.list(path)
    results_list = []
    for filename in file_list:
        results_list.append("/".join([path, filename]))
    return(results_list)

def get_converted_result_path(filename, remote_root, local_root):
    return filename.replace(remote_root, local_root)

def connect(user, password, port, host):
    server = ftpretty(host, user, password, port=port)
    return server

def bulk_download(server, file_list, remote_root, local_root):
    for file in file_list:
        dest_file = file.replace(remote_root, local_root)
        server.get(file, dest_file)
