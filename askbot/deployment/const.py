DEFAULT_PROJECT_NAME = 'askbot_site'
DEFAULT_MEDIA_ROOT_SUBDIR = 'upfiles'

SQLITE = 2
DATABASE_ENGINE_CHOICES = (
    (1, 'PostgreSQL'),
    (SQLITE, 'SQLite'),
    (3, 'MySQL'),
    (4, 'Oracle')
)

YELLOW = '\033[33m'
RED = '\033[31m'
BOLD = '\033[1m'
RESET = '\033[0m'

def bold(text):
    return RED + BOLD + text + RESET

ROOT_DIR_HELP = 'the ' + bold('Root') + \
        ' directory path (relative or absolute).\nThis directory will contain the Django project\'s manage.py file'

PROJ_NAME_HELP = 'the ' + bold('Project') + \
        ' directory name.\nWill be a subdirectory within the ' + \
        bold('Root') + ' for the settings.py, urls.py files'

MEDIA_ROOT_HELP = 'value of the ' + bold('MEDIA_ROOT') + \
        ' setting for the settings.py file.\n ' + \
        'This directory is for the user uploaded files.\n ' + \
        'Default is /upfiles within the ' + bold('Root') + ' directory.'

DOMAIN_NAME_HELP = 'domain name of your Askbot site. Used for the ' + bold('ALLOWED_DOMAINS') + ' setting.'

LANGUAGE_CODE_HELP = 'two or four letter with a dash language code (e.g. ' + \
        bold('fr') + ', ' + bold('de') + ', ' + bold('zh_CN') + '.\n ' + \
        'Value of the ' + bold('LANGUAGE_CODE') + ' setting.\n ' + \
        'Default value is ' + bold('en') + '.'

DATABASE_ENGINE_HELP = 'database engine, type 1 for PostgreSQL, 2 for SQLite, 3 for MySQL, 4 for Oracle.'
