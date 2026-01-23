from dataclass_wizard import EnvWizard
from django_vises.django_settings.env_var import EnvVarAbc


class EnvVar(EnvVarAbc, EnvWizard):

    class _(EnvWizard.Meta):
        env_file = True

    PELICAN_SITES: str = ""
    PUBLISHER_WORKING_PATH: str = "/tmp"
    PUBLISHER_OUTPUT_PATH: str = "/tmp"

    PELICAN_PUBLISHER_PREFIX: str = ""


EV = EnvVar()
EV.PELICAN_PUBLISHER_PREFIX = EV.PELICAN_PUBLISHER_PREFIX.strip(" /").rstrip(" /")
