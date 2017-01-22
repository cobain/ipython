from fabric.api import run, env, local

env.hosts = ['root@dev.mynimble.cn']

def taskA():
    run('ls')

# def taskB():
#     run('whoami')

def test():
    local('git status')