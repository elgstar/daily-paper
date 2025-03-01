#!/usr/bin/python3
# -*- coding: utf-8 -*-
# written by Liangjin Song on 20240316 at Nanchang University
import os, sys, subprocess

class sync:
    def __init__(self):
        self.cwd = os.getcwd()
        # os.chdir('../')
        self.pwd = os.getcwd()
        self.git = 'git'
    def pull(self, branch = 'main'):
        out = subprocess.run(self.git + ' pull origin ' + branch,
                             shell = True, capture_output = True, text = True)
        print(out.stdout.strip())
        print(out.stderr.strip())
        if out.returncode == 0:
            return True
        else:
            return False
    def add(self, files = '--all'):
        os.system(self.git + ' add ' + files)
    def commit(self, message):
        os.system(self.git + ' commit -m "' + message + '"')
    def push(self, branch = 'main'):
        out = subprocess.run(self.git + ' push origin ' + branch,
                             shell = True, capture_output = True, text = True)
        print(out.stdout.strip())
        print(out.stderr.strip())
        if out.returncode == 0:
            return True
        else:
            return False
    def execute(self, message = 'daily paper'):
        if not self.pull():
            os.chdir(self.cwd)
            return False
        self.add()
        self.add()
        self.commit(message)
        if not self.push():
            os.chdir(self.cwd)
            return False
    def force_push(self, branch = 'main'):
        if not self.pull(branch = branch):
            os.chdir(self.cwd)
            return False
        os.system(self.git + ' checkout --orphan latest_branch')
        self.add()
        os.system(self.git + ' commit -am "daily paper"')
        os.system(self.git + ' branch -D ' + branch)
        os.system(self.git + ' branch -m ' + branch)
        out = subprocess.run(self.git + ' push -f origin ' + branch,
                             shell = True, capture_output = True, text = True)
        print(out.stdout.strip())
        print(out.stderr.strip())
        if out.returncode == 0:
            os.chdir(self.cwd)
            return True
        else:
            os.chdir(self.cwd)
            return False

class parser:
    def __init__(self):
        self.sync = sync()
    def __help__(self):
        print('Usage: python3 sync.py [commit message/force push]')
    def parse(self):
        if len(sys.argv) == 1:
            if self.sync.execute():
                print('synchronized successfully!')
            else:
                print('synchronized failed!')
        elif len(sys.argv) == 3:
            if sys.argv[1] == 'force' and sys.argv[2] == 'push':
                if self.sync.force_push():
                    print('force pushed successfully!')
                else:
                    print('force pushed failed!')
            elif sys.argv[1] == 'commit':
                if self.sync.execute(sys.argv[2]):
                    print('synchronized successfully!')
                else:
                    print('synchronized failed!')
            else:
                self.__help__()
        else:
            self.__help__()


if __name__ == '__main__':
    parser().parse()
