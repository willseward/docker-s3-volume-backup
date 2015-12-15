import os
from docker import Client
from stat import S_ISDIR, ST_MODE

def get_all_containers(client):
    return client.containers()

def get_docker_volumes(client, container):
    container_info = client.inspect_container(container['Id'])
    mounts = [mount['Source'] for mount in container_info['Mounts']]
    return mounts

def create_targz_for_volume(volume_path):
    pass

def main():
    client = Client(base_url='unix://var/run/docker.sock', version='auto')
    containers = get_all_containers(client)
    for container in containers:
	print("Searching container: %s" % container['Names'][0])
        vols = get_docker_volumes(client, container)
	for vol in vols:
	    print("    Found volume mounted to %s" % vol)
	    new_path = '/data/' + vol
	    new_path = os.path.normpath(new_path)
	    stat = os.stat(new_path)[ST_MODE]
	    if S_ISDIR(stat):
		print("        Creating tar.gz...")
	    	create_targz_for_volume(new_path)
		print("        Done.")
	    else:
		print("        Skipping, volume is only a file")

if __name__ == "__main__":
    main()
