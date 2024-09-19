# Desc

Rotate many linux user password in many vms at once.

Changing user password on linux was one of security demand, but change it one by one in one vm boring and repetitive well it can be done with enterprise cyber security tools(i.e: cyberark or vault(?)) but yeah i'm cheap af and need ~~the opensource~~ free one. after i googling I only found valut can do it butttt they have many bunch steps and install agent and do this and do that bla bla bla.

Because of that i create simple ansible password rotate the idea was for rotate many linux users in many vms at once and automatically.

## How to use
first create a csv file with format *username*,*password*, and *vm name* or you can see at [example](example.csv) and then generate the variable with *generator.py*

```bash
root@ansible:~/ansible-rotate-password# python3 generator.py -f example-csv.csv 
```

you can add `-g` args for generate random password also you can see the variable in `vars/<VM NAME>/user_list.yaml`.

then edit the *inventory.ini* with your vms ip,root username,keyring.

and finally run the ansible.

```bash
root@ansible:~/ansible-rotate-password# ansible-playbook main.yaml -i inventory.ini
```

## Note
you can add `no_log: true` in each task if you want hide the password showing in terminal when you running the ansible