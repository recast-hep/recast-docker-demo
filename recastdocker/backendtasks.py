import logging
import subprocess
import time
import os

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('RECAST')

def recast(ctx):
  workdir = 'workdirs/{}'.format(ctx['jobguid'])
  dockerimage = ctx['dockerimage']

  cmd = 'docker run -v {}:/workdir {} /workdir /workdir/inputs/context.yaml'.format(
      os.path.abspath(workdir),
      dockerimage)

  with open('{}/docker.log'.format(workdir),'w') as dockerlog:
    proc = subprocess.check_call(cmd,shell=True, stderr = subprocess.STDOUT, stdout = dockerlog)

  log.info('finished successfully')