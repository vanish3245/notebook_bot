from os import getenv
from dataclasses import dataclass

from sqlalchemy.engine import URL

@dataclass
class DatabaseConfig:

    name: str = getenv("POSTGRES_DATABASE")
    user: str = getenv("POSTGRES_USER", "docker")
    passwd: str = getenv("POSTGRES_PASSWORD", None)
    port: int = int(getenv("POSTGRES_PORT", 5432))
    host: str = getenv("POSTGRES_HOST", "db")

    driver: str = "asyncpg"
    database_system: str = "postgresql"

    def build_connection_str(self) -> str:

        return URL.create(
            drivername=f"{self.database_system}+{self.driver}",
            username=self.user,
            database=self.name,
            password=self.passwd,
            port=self.port,
            host=self.host,
        ).render_as_string(hide_password=False)


@dataclass
class RedisConfig:

    host: str = getenv("REDIS_HOST", "redis")
    port: int = int(getenv("REDIS_PORT", 6379))
    passwd: int = getenv("REDIS_PASSWORD")
    state_ttl: int = getenv("REDIS_TTL_STATE", None)
    data_ttl: int = getenv("REDIS_TTL_DATA", None)

@dataclass
class BotConfig:
    token: str = getenv("TOKEN")

@dataclass
class Configuration:
    bot = BotConfig()

    db = DatabaseConfig()
    redis = RedisConfig()



conf = Configuration()