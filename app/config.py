from typing import Optional

from dotenv import find_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import (
    PostgresDsn,
)


class DBSetting(BaseSettings):
    """
    Database settings
    :return DB URL in format: postgresql+asyncpg://user:password@host:port/database
    """
    CONNECTOR: Optional[str] = None
    SCHEME: Optional[str] = None
    PG_HOST: Optional[str] = None
    PG_PORT: Optional[int] = None
    PG_USER: Optional[str] = None
    __PG_PASS: Optional[str] = None
    PG_DB: Optional[str] = None

    model_config = SettingsConfigDict(
        env_file=find_dotenv('.env'),
        env_file_encoding='utf-8',
        extra='ignore',
    )

    @property
    def db_url(self):
        url = PostgresDsn.build(
            scheme=f'{self.SCHEME}+{self.CONNECTOR}',
            username=self.PG_USER,
            password=self.__PG_PASS,
            host=self.PG_HOST,
            path=self.PG_DB,
            port=self.PG_PORT,
        )
        return str(url)


class ProjectSettings(BaseSettings):

    LOG_LEVEL: Optional[str] = 'debug'
    TESTING: Optional[bool] = False
    PROJECT_NAME: Optional[str] = 'Musichat'
    VERSION: Optional[str] = '0.0.1'
    DESCRIPTION: Optional[str] = 'Musichat'
    API_PREFIX: Optional[str] = '/api'
    __SECRET_KEY: Optional[str] = 'SECRET_KEY'

    model_config = SettingsConfigDict(
        env_file=find_dotenv('.env'),
        env_file_encoding='utf-8',
        extra='ignore',
    )


DB = DBSetting(_env_file=find_dotenv('.env'))
settings = ProjectSettings(_env_file=find_dotenv('.env'))

if __name__ == '__main__':
    print(DB.db_url)
    print(settings)


