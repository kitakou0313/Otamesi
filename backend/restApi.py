from kubernetes import client, config
from helper import containerMaker


def main():
    config.load_incluster_config()
    apps_v1 = client.AppsV1Api()  # for server deployment
    core_v1_api = client.CoreV1Api()  # for LB deployment

    deployment = containerMaker.create_deployment_object()
    response = core_v1_api.list_pod_for_all_namespaces(watch=False)

    for pod in response.items:
        if("npmdev" in pod.metadata.name):
            print(pod.metadata.name)

    containerMaker.delete_deployment(apps_v1)
    containerMaker.delete_LoadBalancer(core_v1_api)


if __name__ == '__main__':
    main()
