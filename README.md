# CV_2024_STREAMLIT
- repo for personal webpage made with Streamlit and `st.navigation`

## 4 pages:
- `about me`
- `resume`
- `portfolio`
- `add comments`:
    - this connects to `Google Firebase` where comments are stored using this `pydantic` model:

```py
class Form(BaseModel):
'''a simple validation form

:param _type_ BaseModel: _description_
'''
name: str = Field(description='the name of the user', min_length=1)
email: EmailStr = Field(description='the email of the user')
comment: str | None = Field(default = None, description='the comment left by the user')
time: str = Field(description='the time at which the comment what made')
```

## Logging
Since the app is deployed on `Render`, a simple logging message is used to track activity on the webpage.

## Firestore database
`Firebase` credentials are serialized during initialization from `pydantic` base Settings:

```py
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
```
## Build Documentation
```
mkdocs build
mkdocs serve -a localhost:8001
```

## TO DO
- add testing