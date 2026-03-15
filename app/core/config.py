from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic_settings.sources import YamlConfigSettingsSource
from pathlib import Path


class Settings(BaseSettings):
    """Application settings loaded from environment variables and config files."""

    # ROM library configuration
    rom_library_path: Path = Path.home() / "roms"  # Default to ~/roms
    rom_library_media_path: Path = Path.home() / "roms" / "media"  # Default media path

    # Application configuration
    log_level: str = "INFO"

    # Database configuration
    database_url: str = "sqlite:///rom_library.db"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="ROM_LIBRARY_",
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls,
        init_settings,
        env_settings,
        dotenv_settings,
        file_secret_settings,
    ):
        return (
            init_settings,
            env_settings,
            dotenv_settings,
            YamlConfigSettingsSource(settings_cls, yaml_file="config.yaml"),
            file_secret_settings,
        )


# Create a global settings instance
settings = Settings()