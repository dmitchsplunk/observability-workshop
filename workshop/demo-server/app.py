from kubernetes import client, config, utils
from flask import Flask, json, jsonify, request
from os import path
import yaml
import pandas as pd

app = Flask(__name__)

config.load_kube_config()

core_v1 = client.CoreV1Api()
apps_v1 = client.AppsV1Api()
api = client.ApiClient()

@app.route('/pods', methods=['GET'])
def get_pods():
    result = core_v1.list_pod_for_all_namespaces(_preload_content=False)
    pods = json.loads(result.data)
    df = pd.DataFrame(columns=["Namespace", "Name", "Status", "Pod IP"])

    for r in pods['items']:
        row = (r["metadata"]["namespace"], r["metadata"]["name"], r["status"]["phase"], r["status"]["podIP"])
        df.loc[len(df)] = row

    return df.to_dict(orient='records')


@app.route('/health', methods=['GET'])
def health():
    return "OK"


@app.route('/apply_deployment', methods=['POST'])
def deployment():
        deployment = "deployment.yaml"
        #resp = apps_v1.create_namespaced_deployment(
        #    body=deployment, namespace=namespace, _preload_content=False)
        resp = utils.create_from_yaml(api, deployment, namespace="default")
        print(resp)
        return "200"

@app.route('/delete_deployment', methods=['GET'])
def delete_deployment():
    filename = request.args.get('type', default = 'deployment.yaml', type = str)
    namespace = request.args.get('namespace', default = 'default', type = str)
    resp = apps_v1.delete_namespaced_deployment(name="nginx-deployment", namespace=namespace, _preload_content=False)
    return resp

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=8083, debug=True)