from dataclass_wizard import EnvWizard
from django_vises.django_settings.env_var import EnvVarAbc


class EnvVar(EnvVarAbc, EnvWizard):

    class _(EnvWizard.Meta):
        env_file = True

    HOST_URL_PATH_PREFIX: str = ""

    PELICAN_SITES: str = ""
    PELICAN_WORKING_PATH: str = "/tmp"
    PELICAN_OUTPUT_PATH: str = "/tmp"


EV = EnvVar()
EV.HOST_URL_PATH_PREFIX = EV.HOST_URL_PATH_PREFIX.strip(" /").rstrip(" /")
