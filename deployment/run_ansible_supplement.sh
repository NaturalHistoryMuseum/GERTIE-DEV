#!/bin/bash
# GERTIE Ansible Supplement - Use AFTER sync_to_slaves.sh

echo "========================================="
echo "GERTIE ANSIBLE DEPLOYMENT SUPPLEMENT"
echo "========================================="
echo ""
echo "IMPORTANT: This supplements sync_to_slaves.sh"
echo "Make sure you've run sync_to_slaves.sh FIRST!"
echo ""
read -p "Have you run sync_to_slaves.sh? (y/n): " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    echo "Please run sync_to_slaves.sh first, then return here."
    exit 1
fi

# Check if ansible is installed
if ! command -v ansible-playbook &> /dev/null
then
    echo "Ansible not found. This is optional - continue using sync_to_slaves.sh"
    exit 0
fi

# Run supplemental deployment
ansible-playbook -i inventory.ini deploy.yml
