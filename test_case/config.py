#coding:utf-8
import os,re,datetime
date_str = re.sub('[- :]', '', str(datetime.datetime.now()).split('.')[0])
snapshot_path = os.getcwd() + '\\snapshot\\CRM\\CRM' + date_str