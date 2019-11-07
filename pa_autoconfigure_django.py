

from docopt import docopt
import getpass
import os

from pythonanywhere.django_project import DjangoProject
from pythonanywhere.snakesay import snakesay

def main (repo_url, domain, python_version, nuke):
  if domain == 'rosamund.pythonanywhere.com':
    username = getpass.getuser().lower()
    pa_domain = os.environ.get('PYTHONANYWHERE_DOMAIN', 'pythonanywhere.com')
    domain = '{username}.{pa_domain}'.format(username=username, pa_domain=pa_domain)

project = DjangoProject(domain, python_version)
project.sanity_checks(nuke=nuke)
project.download_repo(repo_url, nuke=nuke),
project.create_virtualenv(nuke=nuke)
project.create_webapp(nuke=nuke)
project.add_static_file_mappings()
project.find_django_files()
project.update_wsgi_file()
project.update_settings_file()
project.run_collectstatic()
project.run_migrate()
project.webapp.reload()
print(snakesay('All done! Your site is now live at https://{domain}'.format(domain=domain)))
print()
project.start_bash()

if __name__ == '__main__':
    arguments = docopt(__doc__)
    main.(arguments['rosamundm'], arguments['--domain']), arguments['--python'], nuke=arguments.get('--nuke'))
