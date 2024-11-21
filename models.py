from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, SecretStr, field_serializer, Field, EmailStr

class Settings(BaseSettings):
    """model to define the app settings

    :param BaseSettings:
    """
    OPENAI_API_KEY: SecretStr | None = None
    OPEN_AI_MODEL_4o_MINI: str| None = None
    OPEN_AI_MODEL_4o: str| None = None

    model_config = SettingsConfigDict(env_file=".env")

    @field_serializer('OPENAI_API_KEY')
    def dump_secret(self, v):
        return v.get_secret_value()
    

class FirebaseSettings(BaseSettings):
    """model to define the firebase connection settings

    :param  BaseSettings:
    """
    type : str| None = None
    project_id: SecretStr | None = None
    private_key_id: SecretStr | None = None
    private_key: SecretStr| None = None
    client_email: SecretStr| None = None
    client_id: SecretStr| None = None
    auth_uri: str| None = None
    token_uri: str| None = None
    auth_provider_x509_cert_url: str| None = None
    client_x509_cert_url: SecretStr| None = None
    universe_domain: str| None = None

    model_config = SettingsConfigDict(env_file=".env.firebase")

    @field_serializer('project_id', 'private_key_id', 'private_key', 'client_email', 'client_id', 'client_x509_cert_url')
    def dump_secret(self, v):
        return v.get_secret_value()
    

class Form(BaseModel):
    """a simple validation form

    :param _type_ BaseModel: _description_
    """
    name: str = Field(description="the name of the user", min_length=1)
    email: EmailStr = Field(description="the email of the user")
    comment: str | None = Field(default = None, description="the comment left by the user")
    time: str = Field(description="the time at which the comment what made")


class ResponseModel(BaseModel):
    """

    :param _type_ BaseModel: _description_
    """
    on_topic: bool = Field(description="""
    Is the topic of the user's query in relation to the allowed topics ? 
    The allowed topics are:
    1. Jonathan Bouchet's resume, curriculum vitae, education, technical skills
    2. Jonathan Bouchet's past and current work experience
    3. Jonathan Bouchet's data analysis, such as tools and techniques used for data analysis
    4. Jonathan Bouchet's publications""")
    topic: str = Field(description="the topic of the query")
    on_topic_confidence_score: float = Field(description="""
    - the confidence score associated to the `on_topic` field.
    - a numerical value between 0 and 1:
    0 is you are not confident of your result
    1 is you are sure of your result
    """)