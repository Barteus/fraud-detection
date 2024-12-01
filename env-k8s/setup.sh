#!/bin/bash

sudo snap install microk8s --channel 1.29-strict
sudo microk8s enable hostpath-storage

sudo snap install juju

juju bootstrap microk8s

#postgresql
juju add-model pg
juju deploy ./env-k8s/pg-bundle.yaml --model pg --trust

juju status --watch 1s

juju run data-integrator/leader get-credentials -m pg

#kafka
juju add-model kafka
juju deploy ./env-k8s/kafka-bundle.yaml --model kafka --trust

juju status --watch 1s

juju run data-integrator/leader get-credentials -m kafka
