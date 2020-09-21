from kubernetes import client, config
import time

from helper import randomStringGen

DEPLOYMENT_NAME = "ttyd"

config.load_incluster_config()

apps_v1 = client.AppsV1Api()  # for server deployment
core_v1_api = client.CoreV1Api()  # for LB deployment


def create_deployment_object(deployImage):
    # Configureate Pod template container
    container = client.V1Container(
        name="articleimg",
        image=deployImage,
    )

    ttydContainer = client.V1Container(
        name="ttyd",
        image="kitakou0313/ubuntuwithttyd:20.10",
        ports=[client.V1ContainerPort(container_port=7681)],
    )

    # Create and configurate a spec section
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": "ttyd"}),
        spec=client.V1PodSpec(containers=[container, ttydContainer], share_process_namespace=True))
    # Create the specification of deployment
    spec = client.V1DeploymentSpec(
        replicas=1,
        template=template,
        selector={'matchLabels': {'app': 'ttyd'}})
    # Instantiate the deployment object
    deployment = client.V1Deployment(
        api_version="apps/v1",
        kind="Deployment",
        metadata=client.V1ObjectMeta(
            name=DEPLOYMENT_NAME + randomStringGen.genRandomLowerString()),
        spec=spec)

    return deployment


def read_pod_status(podName):
    response = core_v1_api.read_namespaced_pod_status(
        namespace="default", name=podName)
    return response.status.phase


def create_deployment(deployment):
    # Create deployement
    apps_v1.create_namespaced_deployment(
        body=deployment,
        namespace="default")

    time.sleep(5)
    response = core_v1_api.list_pod_for_all_namespaces(watch=False)

    for pod in response.items:
        if("ttyd" in pod.metadata.name):
            return pod.metadata.name


def create_LoadBalancer(deployementName):
    body = client.V1Service(
        api_version="v1",
        kind="Service",
        metadata=client.V1ObjectMeta(
            name=deployementName
        ),
        spec=client.V1ServiceSpec(
            type="LoadBalancer",
            selector={"app": "ttyd"},
            ports=[client.V1ServicePort(
                port=7681,
                target_port=7681
            )]
        )
    )
    response = core_v1_api.create_namespaced_service(
        namespace="default", body=body)
    print("Service LoadBalancer created. status='%s'" % str(response.status))


def delete_LoadBalancer(deployementName):
    response = core_v1_api.delete_namespaced_service(
        name=deployementName, namespace="default", body=client.V1DeleteOptions(
            propagation_policy='Foreground',
            grace_period_seconds=5))

    print("Services deleted. status='%s'" % str(response.status))


def update_deployment(api_instance, deployment):
    # Update container image
    deployment.spec.template.spec.containers[0].image = "nginx:1.16.0"
    # Update the deployment
    api_response = api_instance.patch_namespaced_deployment(
        name=DEPLOYMENT_NAME,
        namespace="default",
        body=deployment)
    print("Deployment updated. status='%s'" % str(api_response.status))


def delete_deployment(deploymentName):
    # Delete deployment
    api_response = apps_v1.delete_namespaced_deployment(
        name=deploymentName,
        namespace="default",
        body=client.V1DeleteOptions(
            propagation_policy='Foreground',
            grace_period_seconds=5))
    print("Deployment deleted. status='%s'" % str(api_response.status))
