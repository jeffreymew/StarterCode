# Note: please make a copy of this file for production purposes and do not check it in to Github
import os

AZ_GROUP = "appsvc_rg_Linux_CentralUS"
AZ_LOCATION = "centralus"


def setEnvironmentVariables():
    os.environ["AZ_GROUP"] = AZ_GROUP
    os.environ["AZ_LOCATION"] = AZ_LOCATION
    os.environ["POSTGRES_SERVER_NAME"] = "asdfasdf" # TODO set this variable
    os.environ["POSTGRES_ADMIN_USER"] = "asdgasdg" # TODO set this variable
    os.environ["POSTGRES_ADMIN_PASSWORD"] = "asdgadsg123!" # TODO set this variable
    os.environ["APP_DB_NAME"] = "asdgasdgads" # TODO set this variable
