#!/bin/bash

sudo snap remove microk8s --purge

sudo snap remove juju --purge
rm -Rf ~/.local/share/juju


