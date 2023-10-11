# Introduction to Docker

While Docker might not be a fundamental tools needed for CNO development, you might need to know basic Docker commands for other exercises and personal studies. The following tutorial assumes you are working on a Debian Linux machine (like Kali / Ubuntu).

# Step 1 — Installing Docker

Docker can be installed from the official Ubuntu repository. 

Let's start by updating the host's list of packages:

```bash
sudo apt update
```

The next step is to install Docker itself.

Make sure you are about to install from the Docker repo instead of the default Ubuntu repo:

```bash
sudo apt install docker-io docker-compose
```

Docker and Docker Compose should be installed, started, and enabled at startup. 

Check that the daemon is running.

```bash
sudo systemctl status docker
```

The console output be should similar to the example below showing the service active and running:

```
output:

```

Now you can start to use the docker command line tools to run the exercises provided.

# Step 2 — Add user to group

While it is possible to use `sudo` to run the Docker commands. It's easier to setup Docker by adding the current user to the Docker group.

If you try to execute the Docker command without using sudo or without being a member of the Docker group, you will receive an output similar to the following:

```
Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/containers/json": dial unix /var/run/docker.sock: connect: permission denied
```

Check that the docker daemon is running on this host?

See `docker run --help`.

We can simple fix this problem by the command below:

```
sudo usermod -aG docker ${USER}
```
Apply the new group membership, log out of the server and back in, or type the following:

```
su - ${USER}
```

```
Why do the group permissions require a new login to take effect?
```

Verify that your user has been successfully added to the Docker group by entering the following command:

```
groups
```
 What output did you recieve?
```
output: 

```

# Docker Commands

The scope of this section is to give you basic docker commands to start using docker.

## docker run

Starting a 

```
docker run -it --name <DOCKER_IMAGE_NAME>  --rm alpine /bin/sh
```

```
output:
```

## docker ps

```
docker ps
```

```
output:
```

## docker stop

```
docker stop <DOCKER_IMAGE_NAME>
```


## docker-compose

Start a docker image from a compose file. 

### Example Docker Compose file

docker_compose.yaml

```
version: '3'
services:
  web:
    image: nginx:alpine
    ports:
      - "80:80"
```


### Start Docker container with logging to stdout
```
docker-compose up
```

```
output:
```

### Start a Docker image in the background from a compose file. 

```
docker-compose up -d
```

```
output:
```

### Stop a Docker image

```
docker-compose down
```

```
output:
```

# Docker Networking Explained (Briefly)

## host

Docker host networking is a networking mode in Docker that allows containers to share the network namespace with the host system. In this mode, containers bypass the container-level network isolation and directly use the networking capabilities of the host machine.

When a container is run in host networking mode, it shares the same network interfaces, IP address, and port space as the host system. This means that the container can bind to network services on the host using the same IP and port configurations. Any network-related operations performed within the container will directly affect the host's network.

## bridge

Docker bridge networking is the default networking mode in Docker, providing a private network bridge for containers to communicate with each other and the outside world. When containers are created, they are automatically connected to a bridge network, which facilitates communication between containers running on the same host.

Docker creates a virtual network bridge, commonly named "docker0," on the host system. This bridge acts as a virtual switch, allowing containers to connect to it and communicate with each other. By default, the bridge network operates in the IP subnet range of 172.17.0.0/16.

Bridge networking is ideal for most use cases and simplifies communication between containers on the same host. It provides an isolated network environment for containers while still allowing connectivity to the host and external networks. However, note that containers running on different hosts cannot communicate with each other through bridge networking, as each host has its own isolated bridge network. In such cases, other networking solutions like overlay networks or third-party networking plugins can be used to establish communication between containers on different hosts.

## macvlan

Docker macvlan networking is a feature that allows containers to have their own unique MAC addresses and network interfaces on a host network. It provides a way to directly connect containers to external networks, enabling them to communicate directly with other devices on the network as if they were physical machines.

When using macvlan networking, Docker creates a virtual network interface for each container with its own MAC address. This enables containers to have their own unique identity on the network, separate from the host or other containers. This is particularly useful in scenarios where you want containers to be directly accessible from other devices on the network or require containers to have their own IP addresses.



```
docker network create -d macvlan \
  --subnet=192.168.32.0/24 \
  --ip-range=192.168.32.128/25 \
  --gateway=192.168.32.254 \
  --aux-address="my-router=192.168.32.129" \
  -o parent=eth0 macnet32
```

```
docker network ls
```

```
output:
```

## ipvlan

Docker IPvlan networking is a networking mode in Docker that enables containers to have their own unique MAC and IP addresses on a physical network. It allows containers to connect directly to the network, appearing as individual devices with their own network identity.


Network Isolation: Unlike Docker bridge networking, which shares a common bridge network among containers, IPvlan networking provides network isolation for each container. Each container connected to the IPvlan network has its own network interface and IP address, separate from other containers.


```
 docker network create -d ipvlan \
    --subnet=192.168.1.0/24 \
    --gateway=192.168.1.1 \
    -o ipvlan_mode=l2 \
    -o parent=eth0 db_net
 Start a container on the db_net network
 docker run --net=db_net -it --rm alpine /bin/sh
```

```
docker network ls
```

```
output:
```

# References:

https://docs.docker.com/network/drivers/
